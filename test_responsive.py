import pytest

@pytest.mark.parametrize("width,height", [(375, 812), (768, 1024), (1365, 900)])
def test_homepage_has_no_horizontal_overflow(page, base_url, width, height):
    page.set_viewport_size({"width": width, "height": height})
    page.goto(base_url, wait_until="domcontentloaded")
    dimensions = page.evaluate('''() => ({
        documentWidth: document.documentElement.scrollWidth,
        viewportWidth: document.documentElement.clientWidth
    })''')
    assert dimensions["documentWidth"] <= dimensions["viewportWidth"] + 1, \
        f"Horizontal overflow at {width}px: {dimensions}"
