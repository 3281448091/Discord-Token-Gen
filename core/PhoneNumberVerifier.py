# verifies the phone number

import requests
import core.Solver4d
import core.Log4p
import time

class Verify:

    def __init__(self,ptoken, stoken,dtoken,dpwd):

        self.ptoken = ptoken

        self.stoken = stoken

        self.dtoken = dtoken

        self.Solver = core.Solver4d.Solver(stoken)

        self.Logger = core.Log4p.Logger()

        self.dpwd = dpwd




    def verify_phone_number(self):
        try:
            result = requests.get(f"https://onlinesim.ru/api/getNum.php?apikey={self.ptoken}&service=discord&number=true&country=7").json()
        except Exception as e:
            self.Logger.error(__name__,"problem while registering a phone number task - "+str(e))

        # phone number
        number = result.get("number")

        self.Logger.info(__name__, "using "+number)

        tzid = result.get("tzid")

        self.Logger.info(__name__, "succesfully registered phone number verfication task")

        json = {
            "captcha_key": self.Solver.get_captcha_key(True),
            "change_phone_reason":"user_action_required",
            "phone" : number,
        }

        headers = {
          "accept": "*/*",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "it",
          "authorization": self.dtoken,
          "content-type": "application/json",
          "origin": "https://discord.com",
          "referer": "https://discord.com/channels/@me",
          "sec-ch-ua":'Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93',
          "sec-ch-ua-mobile": "?0",
          "sec-ch-ua-platform": "Windows",
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny44MiBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTMuMC40NTc3LjgyIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2NvcmQuY29tL2xvZ2luIiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NjYyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
        }
        try:
            with requests.post("https://discord.com/api/v9/users/@me/phone", json=json, headers=headers) as response:
                pass #expects no response
        except Exception as e:
            self.Logger.error(__name__,"problem while initing phone number verficiation request - "+str(e))

        self.Logger.info(__name__, "requested phone number verify")



        while True:
            with requests.get(f"https://onlinesim.ru/api/getState.php?apikey={self.ptoken}&tzid={tzid}") as response:
                if response.json()[0].get("msg") != None:
                    code = response.json()[0].get("msg")
                    break
                else:
                    time.sleep(1)
        self.Logger.info(__name__, "got sms")
        json = {
            "code" : code,
            "phone" : number,
        }
        headers = {
          "accept": "*/*",
          "accept-language": "it",
          "authorization": self.dtoken,
          "content-type": "application/json",
          "origin": "https://discord.com",
          "referer": "https://discord.com/channels/@me",
          "sec-ch-ua":
            'Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93',
          "sec-ch-ua-mobile": "?0",
          "sec-ch-ua-platform": "Windows",
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny44MiBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTMuMC40NTc3LjgyIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2NvcmQuY29tL2xvZ2luIiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NjYyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
        }

        with requests.post("https://discord.com/api/v9/phone-verifications/verify",json=json,headers=headers) as response:
            final_token = response.json()['token']

        json = {
            "phone_token" : final_token,
            "password" : self.dpwd,
            "change_phone_reason" : "user_action_required",
        }

        self.Logger.info(__name__, "requested change")

        headers = {
          "accept": "*/*",
          "accept-language": "it",
          "authorization": self.dtoken,
          "content-type": "application/json",
          "origin": "https://discord.com",
          "referer": "https://discord.com/channels/@me",
          "sec-ch-ua":
            'Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93',
          "sec-ch-ua-mobile": "?0",
          "sec-ch-ua-platform": "Windows",
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny44MiBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTMuMC40NTc3LjgyIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2NvcmQuY29tL2xvZ2luIiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NjYyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
        }

        with requests.post("https://discord.com/api/v9/users/@me/phone",json=json,headers=headers) as response:
            pass

        self.Logger.info(__name__, "complete")

# OTU0MTA1OTkxMTI4MDUxNzEy.YjOUYQ.l7uHs33Osov8cSDL-ikY2R0m7S8

















