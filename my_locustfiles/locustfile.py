from locust import HttpUser, TaskSet, task, between
from prometheus_client import start_http_server, Gauge
import time
import threading

class UserBehavior(TaskSet):

    @task
    def browse(self):

        self.client.get("/")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
   

def start_prometheus_server():
    start_http_server(8000)  # Porta onde as métricas serão expostas
    print("Prometheus metrics available on port 8000")


if __name__ == "__main__":
    # Inicie o servidor Prometheus em um thread separado
    prometheus_thread = threading.Thread(target=start_prometheus_server)
    prometheus_thread.start()

    # Inicie o Locust
    from locust.main import main
    main()
