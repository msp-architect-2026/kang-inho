from locust import HttpUser, task, between
import random

class BoardUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        self.client.post("/login", data={
            "username": "admin",
            "password": "asdf1234"
        }, allow_redirects=True)
    
    @task(3)
    def view_main(self):
        self.client.get("/main")
    
    @task(2)
    def view_post(self):
        post_id = random.randint(1, 253)
        self.client.get(f"/post/{post_id}")
    
    @task(1)
    def write_post(self):
        self.client.get("/write")
        self.client.post("/write", data={
            "title": f"성능 테스트 게시글 {random.randint(1,1000)}",
            "content": "Locust 성능 테스트 내용입니다."
        }, allow_redirects=True)
