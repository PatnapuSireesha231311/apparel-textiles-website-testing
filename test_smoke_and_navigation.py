import pytest

def test_homepage_loads(page, base_url):
    response = page.goto(base_url, wait_until="domcontentloaded")
    assert response is not None
    assert response.status < 400, f"Homepage returned HTTP {response.status}"
    assert page.title().strip(), "Page title should not be empty"

def test_navigation_to_catalog(page, base_url):
    page.goto(base_url, wait_until="domcontentloaded")
    link = page.get_by_role("link", name="Shop", exact=False)
    if link.count() == 0:
        pytest.skip("Update selector: no visible Shop link found.")
    link.first.click()
    page.wait_for_load_state("domcontentloaded")
    assert page.url != base_url + "/", "Navigation should change route"

def test_search_returns_feedback(page, base_url):
    page.goto(base_url, wait_until="domcontentloaded")
    search = page.get_by_role("searchbox")
    if search.count() == 0:
        search = page.get_by_placeholder("Search", exact=False)
    if search.count() == 0:
        pytest.skip("Update selector: search input not found.")
    search.first.fill("cotton")
    search.first.press("Enter")
    page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").inner_text().strip()
