# Apparel & Textiles Website — Testing Framework

A starter suite for browser-level functional tests with Playwright/pytest and an optional Locust HTTP load test.

## Important
This is a template, not proof that a live website passed testing. Set `BASE_URL` and adapt selectors/routes to your site. Use staging and payment-provider sandbox credentials only. Do not load-test production or submit real payments without authorization.

## Setup
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```
Copy `.env.example` to `.env`, set `BASE_URL`, then run:
```bash
pytest -v
```
Optional load test, authorized staging only:
```bash
locust -f performance/locustfile.py --host http://127.0.0.1:8000
```
Adapt the routes, accessible labels, and product selectors in tests to your website. Stable `data-testid` attributes are recommended.
