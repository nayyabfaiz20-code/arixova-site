# Arixova Tech website starter

A lightweight, responsive website for Arixova Tech. It uses plain HTML, CSS and JavaScript with a small Python standard-library server for secure server-side enquiry delivery. There are no JavaScript package dependencies.

## Run locally

1. Install Python 3.10 or later.
2. From this folder, run `python build_site.py` to generate the route pages.
3. Configure the environment variables described below if you want to test actual email delivery.
4. Run `python server.py` and open `http://127.0.0.1:8000`.

Without SMTP configuration, the form intentionally shows a delivery error and the fallback email address; it does not pretend an enquiry was sent. The pages themselves can be previewed without SMTP.
Run `python -m unittest discover -s tests` to exercise form validation, rate limiting, same-origin checks and the SMTP handoff with a mocked provider.

## Routes

- `/` — homepage
- `/about/` — about
- `/services/` — services overview
- `/services/web-development/`
- `/services/website-management/`
- `/services/custom-tools/`
- `/services/ai-integration/`
- `/services/workflow-automation/`
- `/services/digital-strategy/`
- `/contact/` — consultation form
- `/privacy/` and `/cookies/` — policy drafts for owner review

Service pages are generated from the `SERVICES` data in `build_site.py`. Edit that content and run the build script again to update the pages. Shared layout and navigation are generated in the same script; global styling lives in `site.css`.

## Enquiry email setup

Set these environment variables on the server (do not put real credentials in source control):

- `SMTP_HOST` — SMTP provider hostname
- `SMTP_PORT` — usually `587` for STARTTLS, or the provider's SSL port
- `SMTP_USERNAME` and `SMTP_PASSWORD` — provider credentials, if required
- `SMTP_FROM` — sender address authorised by the provider
- `ENQUIRY_TO` — mailbox that should receive website enquiries
- `SMTP_USE_STARTTLS` — defaults to `true`
- `SMTP_USE_SSL` — set to `true` for implicit TLS instead of STARTTLS

The endpoint validates input on the server, limits payload size, checks same-origin requests, uses a honeypot and limits each client address to five submissions per hour per running process. For a public deployment, also configure HTTPS, edge-level rate limiting, monitored email delivery and the correct trusted-proxy settings for the hosting platform. The included Python server is a starter deployment option, not a replacement for production operations review.

## Before publishing

- Confirm the brand, service copy, email address and any location/company claims with the business owner.
- Review the privacy and cookie drafts with the organisation's privacy adviser. Confirm the lawful basis, retention and deletion process, hosting logs and email provider.
- The site loads Sora and Inter from Google Fonts. Self-host appropriately licensed font files if third-party font requests are not wanted.
- Update the sitemap and robots sitemap URL in `build_site.py` to the final domain, then run `python build_site.py`.
- Configure a production host with HTTPS and a supported Python runtime for the enquiry endpoint. A static-only host cannot run `server.py`.
- Verify form submission with real SMTP credentials in a staging environment before publishing.

## Design and motion

The shared content container uses a 1550px maximum width with fluid side padding. The design pairs Sora headings with Inter body copy, follows the supplied navy/blue palette, and uses small CSS-only geometry and reveal transitions. Motion respects `prefers-reduced-motion`; content stays visible when JavaScript is unavailable.
