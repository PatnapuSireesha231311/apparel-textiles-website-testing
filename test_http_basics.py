import requests

def test_homepage_http_response(base_url):
    response = requests.get(base_url, timeout=10)
    assert response.status_code < 400
    assert response.elapsed.total_seconds() < 3.0, \
        f"Response took {response.elapsed.total_seconds():.2f}s (target < 3.0s)"
    assert "text/html" in response.headers.get("content-type", "").lower()
