import pytest

def open_first_product(page, base_url):
    page.goto(base_url, wait_until="domcontentloaded")
    links = page.locator('a[href*="/product"], a[href*="/products/"]')
    if links.count() == 0:
        pytest.skip("No product link found; update selector.")
    links.first.click()
    page.wait_for_load_state("domcontentloaded")

def test_product_detail_has_information(page, base_url):
    open_first_product(page, base_url)
    body = page.locator("body").inner_text().lower()
    assert any(x in body for x in ["size", "colour", "color", "price", "₹", "$"]), \
        "Product page should expose options or pricing"

def test_add_to_cart_flow(page, base_url):
    open_first_product(page, base_url)
    size = page.get_by_label("Size", exact=False)
    if size.count():
        try:
            size.first.select_option(index=1)
        except Exception:
            pass
    button = page.get_by_role("button", name="Add to cart", exact=False)
    if button.count() == 0:
        button = page.get_by_role("button", name="Add to bag", exact=False)
    if button.count() == 0:
        pytest.skip("Update selector: add-to-cart button not found.")
    button.first.click()
    page.wait_for_timeout(500)
    body = page.locator("body").inner_text().lower()
    assert any(x in body for x in ["added", "cart", "bag", "view cart"])

def test_cart_page_is_reachable(page, base_url):
    page.goto(base_url, wait_until="domcontentloaded")
    link = page.get_by_role("link", name="Cart", exact=False)
    if link.count() == 0:
        link = page.get_by_role("link", name="Bag", exact=False)
    if link.count() == 0:
        pytest.skip("Update selector: cart/bag link not found.")
    link.first.click()
    page.wait_for_load_state("domcontentloaded")
    assert page.locator("body").inner_text().strip()
