# Solver for discord
# www.capmonster.cloud

import requests
import core.Log4p

class Solver:
    def __init__(self, token):

        # inits the capmonster token
        self.token = token

        # prepares logger
        self.Logger = core.Log4p.Logger()

        self.Logger.info(__name__,"Solver loaded")

    def get_captcha_key(self,isPhone):
        if isPhone == True:
            token = "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"
        else:
            token = "4c672d35-0701-42b2-88c3-78380b0db560"
        json = {
            "clientKey" : self.token,
            "task" : {
                "type" : "HCaptchaTaskProxyless",
                "websiteURL" : "https://discord.com/",
                "websiteKey" : token,
                "minScore" : 0.3
            }
        }
        with requests.post("https://api.capmonster.cloud/createTask", json=json) as response:
            task_id = response.json().get("taskId")

        json = {
            "clientKey" : self.token,
            "taskId" : task_id
        }

        # keep on looping until getting the token, time efficient.
        while True:
            with requests.get("https://api.capmonster.cloud/getTaskResult", json = json) as response:
                 if "processing" in response.text:
                     pass
                 else:
                    try:
                        return response.json()["solution"]["gRecaptchaResponse"]
                    except Exception:
                        print("YOU NEED https://capmonster.cloud api key and with CREDIT INSIDE, YOU NEED TO PAY!")
                    break


