"""
TODO
1. auto reg
2. cloud nitro sniping
"""
import requests
from colorama import Fore
import secrets
import core.Log4p
import core.Solver4d
import core.PhoneNumberVerifier
import sys
banner =f"""{Fore.BLUE}
███╗░░░███╗██╗░█████╗░░█████╗░██╗░░██╗██╗░░░██╗░█████╗░
████╗░████║██║██╔══██╗██╔══██╗██║░░██║██║░░░██║██╔══██╗
██╔████╔██║██║███████║██║░░██║███████║██║░░░██║███████║
██║╚██╔╝██║██║██╔══██║██║░░██║██╔══██║██║░░░██║██╔══██║
██║░╚═╝░██║██║██║░░██║╚█████╔╝██║░░██║╚██████╔╝██║░░██║
╚═╝░░░░░╚═╝╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝
                                  Author : Senior#6969
{Fore.RESET}
"""

class Settings:
    capmonster = ""
    onlinesimru = ""

class Main:
    def __init__(self):

        # init Logger
        self.Logger = core.Log4p.Logger()

        self.Solver = core.Solver4d.Solver(Settings.capmonster)

        # introduces the banner
        # print(banner) i dont we need banner

        self.reg()

    def reg(self):

        email = f"{secrets.token_hex(8)}@gmail.com"

        self.Logger.info(__name__, email)

        # the password that is going to be needed in the final phone number verifiy
        password = secrets.token_hex(10)

        self.Logger.info(__name__,password)
        param = {
            "username": "%s" % (secrets.token_hex(5)),
            "email": email,
            "password": password,
            "invite": "null",
            "consent": True,
            "captcha_key": self.Solver.get_captcha_key(False)
        }

        headers = {
            "Host": "discord.com",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny42MyBTYWZhcmkvNTM3LjM2IEVkZy85My4wLjk2MS40NyIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAuNDU3Ny42MyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9jaGFubmVscy81NTQxMjU3Nzc4MTg2MTU4NDQvODcwODgxOTEyMzQyODUxNTk1IiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
            "X-Fingerprint": "",
            "Accept-Language": "en-US",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47",
            "Content-Type": "application/json",
            "Authorization": "undefined",
            "Accept": "*/*", "Origin": "https://discord.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://discord.com/register",
            "X-Debug-Options": "bugReporterEnabled",
            "Accept-Encoding": "gzip, deflate, br",
            "Cookie": "OptanonConsent=version=6.17.0; locale=th"
        }

        resp = requests.post("https://discord.com/api/v9/auth/register",json=param,headers=headers)

        token = None

        try:
            token = resp.json()['token']
        except Exception as e:
            sys.exit(0)
            self.Logger.warn(__name__,"Cannot fetch token - "+resp.text)

        self.Logger.info(__name__, "Got token = " + str(token))

        core.PhoneNumberVerifier.Verify(Settings.onlinesimru,Settings.capmonster,token,password).verify_phone_number()

        self.Logger.info(__name__,"finished verifying token phone number")

        verify_headers = {
          "accept": "*/*",
          "accept-language": "it",
          "authorization": token,
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
        json = {
            "captcha_key":""
        }









if __name__ == "__main__":
    Main()


