from locust import HttpLocust, TaskSet

def login(self):
    self.client.post("/login", {"username":"ellen_key", "password":"education"})

def index(self):
    self.client.get("/")

def profile(self):
    self.client.get("/profile")

class UserBehavior(TaskSet):
    tasks = {index:2, profile:1}

    def on_start(self):
        login(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=5000
    max_wait=9000
