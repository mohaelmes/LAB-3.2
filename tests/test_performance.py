from locust import HttpUser, task, between

class APITestUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_items(self):
        self.client.get("/items")

    @task
    def add_item(self):
        self.client.post('/items', json={'name': 'Item from Locust', 'description': 'Test description'})
