import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "http://127.0.0.1:8000").rstrip("/")

@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1365, "height": 900})
        page = context.new_page()
        page.set_default_timeout(8000)
        yield page
        context.close()
        browser.close()
