import os
import dotenv
import json

class ImportConfigsGlobals():
    def __init__(self):
        dotenv.load_dotenv(os.path.join(os.path.dirname(
            __file__), '..', 'configs', 'locust.env'))
        self.HOST = os.getenv("host", "https://www.example.com")
        self.HEADLESS = os.getenv("headless", False)
        self.LOGFILE = os.getenv("logfile", os.path.join(os.path.dirname(
            __file__), '..', 'logs', 'application.DEBUG.log'))
        # if not os.path.exists(self.LOGFILE):
        #     os.path. (self.LOGFILE)
        self.USERS = os.getenv("users", 1)
        self.SPAWN_RATE = os.getenv("spawn-rate", 10)
        self.RUN_TIME = os.getenv("run-time", "5m")
        self.WEB_HOST = os.getenv("web-host", "192.168.15.147")
        self.TAGS = os.getenv("tags", ["NormalTask", "ExecutionTest", "DEBUG"])

    def help(self):
        configurationAtual = {
            "HOST": f"{self.HOST}",
            "HEADLESS": f"{self.HEADLESS}",
            "LOGFILE": f"{self.LOGFILE}",
            "USERS": f"{self.USERS}",
            "SPAWN_RATE": f"{self.SPAWN_RATE}",
            "RUN_TIME": f"{self.RUN_TIME}",
            "TAGS": f"{self.TAGS}",
        }
        configurationJson = json.dumps(configurationAtual,indent=4)
        return print(configurationJson)


# if __name__ == "__main__":
#     configs = ImportConfigsGlobals()
    # configs.help()
