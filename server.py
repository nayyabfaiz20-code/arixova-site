import json
import os
import re
import smtplib
import time
from collections import OrderedDict, deque
from email.message import EmailMessage
from email.utils import parseaddr
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).parent.resolve()
MAX_BODY = 12_000
RATE_WINDOW = 60 * 60
RATE_LIMIT = 5
MAX_TRACKED_ADDRESSES = 10_000
SERVICE_VALUES = {
    "",
    "web-development",
    "website-management",
    "custom-tools",
    "ai-integration",
    "workflow-automation",
    "digital-strategy",
}
EMAIL_RE = re.compile(r"^[^@\s]{1,64}@[^@\s.]+(?:\.[^@\s.]+)+$")
ATTEMPTS = OrderedDict()


def send_enquiry(data: dict) -> None:
    host = os.environ.get("SMTP_HOST", "").strip()
    sender = os.environ.get("SMTP_FROM", "").strip()
    recipient = os.environ.get("ENQUIRY_TO", "").strip()
    if not host or not sender or not recipient:
        raise RuntimeError("Email delivery is not configured. Please email hello@arixova.tech instead.")

    message = EmailMessage()
    message["Subject"] = "New website enquiry — Arixova Tech"
    message["From"] = sender
    message["To"] = recipient
    message["Reply-To"] = data["email"]
    service = data["service"] or "Not specified"
    message.set_content(
        "A new enquiry was submitted through the Arixova Tech website.\n\n"
        f"Name: {data['name']}\n"
        f"Email: {data['email']}\n"
        f"Company: {data['company'] or 'Not provided'}\n"
        f"Service: {service}\n\n"
        f"Message:\n{data['message']}\n"
    )

    port = int(os.environ.get("SMTP_PORT", "587"))
    username = os.environ.get("SMTP_USERNAME", "")
    password = os.environ.get("SMTP_PASSWORD", "")
    timeout = 15
    use_ssl = os.environ.get("SMTP_USE_SSL", "").lower() in {"1", "true", "yes"}
    use_starttls = os.environ.get("SMTP_USE_STARTTLS", "true").lower() in {"1", "true", "yes"}

    if use_ssl:
        with smtplib.SMTP_SSL(host, port, timeout=timeout) as smtp:
            if username:
                smtp.login(username, password)
            smtp.send_message(message)
    else:
        with smtplib.SMTP(host, port, timeout=timeout) as smtp:
            smtp.ehlo()
            if use_starttls:
                smtp.starttls()
                smtp.ehlo()
            if username:
                smtp.login(username, password)
            smtp.send_message(message)


class SiteHandler(SimpleHTTPRequestHandler):
    server_version = "ArixovaSite/1.0"
    sys_version = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; "
            "base-uri 'self'; object-src 'none'; frame-ancestors 'none'; "
            "form-action 'self'; connect-src 'self'; img-src 'self' data:; "
            "script-src 'self'; style-src 'self' https://fonts.googleapis.com; "
            "font-src 'self' https://fonts.gstatic.com",
        )
        super().end_headers()

    def _json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _valid_origin(self) -> bool:
        origin = self.headers.get("Origin")
        if not origin:
            return False
        parsed = urlsplit(origin)
        return parsed.scheme in {"http", "https"} and parsed.netloc.lower() == self.headers.get("Host", "").lower()

    def _rate_limited(self) -> bool:
        now = time.monotonic()
        address = self.client_address[0]
        attempts = ATTEMPTS.pop(address, deque())
        while attempts and now - attempts[0] > RATE_WINDOW:
            attempts.popleft()
        if len(attempts) >= RATE_LIMIT:
            ATTEMPTS[address] = attempts
            return True
        attempts.append(now)
        ATTEMPTS[address] = attempts
        while len(ATTEMPTS) > MAX_TRACKED_ADDRESSES:
            ATTEMPTS.popitem(last=False)
        return False

    def _error(self, status: int, message: str) -> None:
        self._json(status, {"error": message})

    def do_POST(self):
        if urlsplit(self.path).path != "/api/enquiry":
            self._error(404, "This endpoint does not exist.")
            return
        if not self._valid_origin():
            self._error(403, "The request origin could not be verified. Please email hello@arixova.tech.")
            return
        if self._rate_limited():
            self._error(429, "Too many enquiries were submitted from this connection. Please try again later.")
            return
        if self.headers.get_content_type() != "application/json":
            self._error(415, "The enquiry must be submitted as valid form data.")
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self._error(400, "The request size could not be read.")
            return
        if length <= 0 or length > MAX_BODY:
            self._error(413, "The enquiry is empty or too large. Please shorten your message and try again.")
            return
        try:
            data = json.loads(self.rfile.read(length))
        except (json.JSONDecodeError, UnicodeDecodeError):
            self._error(400, "The enquiry could not be read. Please check the form and try again.")
            return
        if not isinstance(data, dict):
            self._error(400, "The enquiry form data is invalid.")
            return

        fields = ("name", "email", "company", "service", "message", "website")
        if any(not isinstance(data.get(field, ""), str) for field in fields):
            self._error(400, "Please check the information in the form.")
            return
        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        company = data.get("company", "").strip()
        service = data.get("service", "").strip()
        message = data.get("message", "").strip()
        if data.get("website", "").strip():
            self._error(400, "The form could not be accepted. Please contact hello@arixova.tech.")
            return
        if not name or len(name) > 100 or not EMAIL_RE.fullmatch(email) or len(email) > 254:
            self._error(400, "Please provide a name and a valid email address.")
            return
        parsed_email = parseaddr(email)[1]
        if parsed_email != email:
            self._error(400, "Please provide a valid email address.")
            return
        if len(company) > 120 or len(message) < 10 or len(message) > 5000 or service not in SERVICE_VALUES:
            self._error(400, "Please check the company, service and message fields.")
            return
        if data.get("consent") is not True:
            self._error(400, "Please confirm you have read the privacy notice.")
            return

        try:
            send_enquiry({
                "name": name,
                "email": email,
                "company": company,
                "service": service,
                "message": message,
            })
        except RuntimeError as error:
            self._error(503, str(error))
            return
        except (smtplib.SMTPException, OSError, ValueError):
            self.log_error("Enquiry email delivery failed.")
            self._error(502, "We could not deliver your enquiry. Please email hello@arixova.tech instead.")
            return

        self._json(201, {"message": "Your enquiry has been sent."})

    def log_message(self, format, *args):
        # Keep submitted personal data out of access logs.
        super().log_message(format, *args)


if __name__ == "__main__":
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "8000"))
    server = ThreadingHTTPServer((host, port), SiteHandler)
    print(f"Arixova site available at http://{host}:{port}")
    print("Configure SMTP_HOST, SMTP_FROM and ENQUIRY_TO for form email delivery.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping website server.")
        server.server_close()
