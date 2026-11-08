import json
import os
import sys
import threading
import unittest
from http.server import ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request, urlopen


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import server


class SMTPStub:
    def __init__(self, *args, **kwargs):
        self.messages = []
        self.calls = []

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def ehlo(self):
        self.calls.append("ehlo")

    def starttls(self):
        self.calls.append("starttls")

    def login(self, username, password):
        self.calls.append(("login", username, password))

    def send_message(self, message):
        self.messages.append(message)


class SiteTests(unittest.TestCase):
    def setUp(self):
        server.ATTEMPTS.clear()
        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), server.SiteHandler)
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()
        self.base = f"http://127.0.0.1:{self.httpd.server_port}"
        self.origin = self.base
        self.addCleanup(self.thread.join, 2)
        self.addCleanup(self.httpd.server_close)
        self.addCleanup(self.httpd.shutdown)

    def payload(self):
        return {
            "name": "Test Person",
            "email": "person@example.com",
            "company": "Example Ltd",
            "service": "web-development",
            "message": "A test enquiry with enough detail.",
            "consent": True,
            "website": "",
        }

    def post(self, payload, origin=None):
        request = Request(
            self.base + "/api/enquiry",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Origin": origin or self.origin,
            },
            method="POST",
        )
        try:
            response = urlopen(request, timeout=3)
        except HTTPError as error:
            response = error
        with response:
            return response.status, json.loads(response.read().decode("utf-8"))

    def test_valid_enquiry_is_accepted(self):
        with patch.object(server, "send_enquiry") as send:
            status, body = self.post(self.payload())
        self.assertEqual(status, 201)
        self.assertIn("sent", body["message"])
        send.assert_called_once()

    def test_invalid_email_is_rejected(self):
        payload = self.payload()
        payload["email"] = "not-an-email"
        with patch.object(server, "send_enquiry") as send:
            status, _ = self.post(payload)
        self.assertEqual(status, 400)
        send.assert_not_called()

    def test_consent_and_honeypot_are_enforced(self):
        with patch.object(server, "send_enquiry") as send:
            payload = self.payload()
            payload["consent"] = False
            consent_status, _ = self.post(payload)
            payload = self.payload()
            payload["website"] = "spam"
            spam_status, _ = self.post(payload)
        self.assertEqual(consent_status, 400)
        self.assertEqual(spam_status, 400)
        send.assert_not_called()

    def test_cross_origin_request_is_rejected(self):
        with patch.object(server, "send_enquiry") as send:
            status, _ = self.post(self.payload(), "https://example.invalid")
        self.assertEqual(status, 403)
        send.assert_not_called()

    def test_rate_limit_is_enforced(self):
        with patch.object(server, "send_enquiry"):
            statuses = [self.post(self.payload())[0] for _ in range(6)]
        self.assertEqual(statuses[:5], [201] * 5)
        self.assertEqual(statuses[5], 429)

    def test_smtp_message_uses_configured_tls_and_reply_address(self):
        smtp = SMTPStub()
        environment = {
            "SMTP_HOST": "smtp.example.com",
            "SMTP_PORT": "587",
            "SMTP_USERNAME": "website",
            "SMTP_PASSWORD": "test-secret",
            "SMTP_FROM": "website@example.com",
            "ENQUIRY_TO": "team@example.com",
            "SMTP_USE_STARTTLS": "true",
            "SMTP_USE_SSL": "false",
        }
        with patch.dict(os.environ, environment, clear=False), patch.object(server.smtplib, "SMTP", return_value=smtp):
            server.send_enquiry(self.payload())
        self.assertEqual(smtp.calls, ["ehlo", "starttls", "ehlo", ("login", "website", "test-secret")])
        self.assertEqual(smtp.messages[0]["To"], "team@example.com")
        self.assertEqual(smtp.messages[0]["Reply-To"], "person@example.com")
        self.assertIn("A test enquiry", smtp.messages[0].get_content())

    def test_missing_smtp_configuration_fails_explicitly(self):
        with patch.dict(os.environ, {"SMTP_HOST": "", "SMTP_FROM": "", "ENQUIRY_TO": ""}, clear=False):
            with self.assertRaisesRegex(RuntimeError, "not configured"):
                server.send_enquiry(self.payload())


if __name__ == "__main__":
    unittest.main()
