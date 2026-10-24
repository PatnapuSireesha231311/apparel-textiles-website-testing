from locust import HttpUser, task, between

class ApparelShopVisitor(HttpUser):
    wait_time = between(1, 3)

    @task(5)
    def browse_homepage(self):
        self.client.get("/", name="GET /")

    @task(3)
    def browse_catalog(self):
        self.client.get("/products", name="GET /products")  # Adapt route.

    @task(2)
    def search_catalog(self):
        self.client.get("/search?q=cotton", name="GET /search")  # Adapt route.
