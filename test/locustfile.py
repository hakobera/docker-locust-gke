from locust import HttpLocust, TaskSet

def login(self):
    self.client.post("/", {"username":"ellen_key", "password":"education"})

def slow(self):
    self.client.get("/slow")

def fast(self):
    self.client.get("/fast")

class UserBehavior(TaskSet):
    tasks = { slow: 1, fast: 3 }

    def on_start(self):
        login(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=100
    max_wait=1000
