"""
TODO
1. auto reg
2. cloud nitro sniping
"""
import random

import requests
import httpx
from colorama import Fore
import secrets
import core.Log4p
import core.Solver4d
import core.PhoneNumberVerifier
import core.Realistic.Faker
from hcaptchabypass import bypass
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
    # random select proxy
    proxy = open("proxies.txt","r").read().split("\n")

    #def get_proxy(self):
    #    proxies = {
    #"https":"http://"+random.choice(self.proxy),
    #"http":"http://"+random.choice(self.proxy)
    #        }
    #    return proxies

    # random select proxy
    proxy = open("proxies.txt","r").read().split("\n")

    def get_proxy(self):
        if open("proxies.txt","r").read() == '':
                proxies = {
                    "https":"http://127.0.0.1",
                    "http":"http://127.0.0.1"
                }
        else:
            proxies = {
        "https":"http://"+random.choice(self.proxy),
        "http":"http://"+random.choice(self.proxy)
                }
            return proxies

class Main:
    def __init__(self):

        # init Logger
        self.Logger = core.Log4p.Logger()

        self.Faker = core.Realistic.Faker.FDiscord()

        self.Solver = core.Solver4d.Solver(Settings.capmonster)

        # introduces the banner
        # print(banner) i dont we need banner

        self.Settings = Settings()

        self.reg()

    def reg(self):

        email = self.Faker._get_fake_email()+"@gmail.com"

        self.Logger.content(__name__,"Email: ", email)

        # the password that is going to be needed in the final phone number verifiy
        password = secrets.token_hex(10)

        self.Logger.content(__name__,"Password: ", password)

        # Reciving cookies

        header1 = {
            "Host": "discord.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            "sec-ch-ua-mobile": "?0",
            "Upgrade-Insecure-Requests": "1",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-us,en;q=0.9",
        }

        getcookie = httpx.get("https://discord.com/register").headers['set-cookie']
        sep = getcookie.split(";")
        sx = sep[0]
        sx2 = sx.split("=")
        dfc = sx2[1]
        split = sep[6]
        split2 = split.split(",")
        split3 = split2[1]
        split4 = split3.split("=")
        sdc = split4[1]

        # Get Fingerprint

        header2 = {
            "Host": "discord.com",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
            "X-Super-Properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Mi4wLjQ1MTUuMTMxIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiI5Mi4wLjQ1MTUuMTMxIiwib3NfdmVyc2lvbiI6IjEwLjE1LjciLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTI3OTIsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
            "X-Context-Properties": "eyJsb2NhdGlvbiI6IlJlZ2lzdGVyIn0=",
            "Accept-Language": "en-US",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            "Authorization": "undefined",
            "Accept": "*/*",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://discord.com/register",
            "Accept-Encoding": "gzip, deflate, br"
        }

        fingerprintres = httpx.get("https://discord.com/api/v9/experiments", timeout=10)

        while True:
            if fingerprintres.text != "":
                fingerprint = fingerprintres.json()['fingerprint']
                break
            else:
                return True

        param = {
            "username": self.Faker._get_fake_username(),
            "email": email,
            "date_of_birth":"1978-06-09",
            "password": password,
            "fingerprint": fingerprint,
            "gift_code_sku_id":"null",
            "invite": "null",
            "consent": "true",
            "captcha_key":  self.Solver.get_captcha_key(False)
        }

        headers = {
            "accept" : "*/*",
            "accept-encoding" : "gzip, deflate, br",
            "accept-language" : "zh-CN,zh;q=0.9,en;q=0.8",
            "content-length":"4797",
            "content-type":"application-json",
            "cookie":f"__dcfduid={dfc}; __sdcfduid={sdc}; _gcl_au=1.1.33345081.1647643031; _ga=GA1.2.291092015.1647643031; _gid=GA1.2.222777380.1647643031; OptanonConsent=isIABGlobal=false&datestamp=Fri+Mar+18+2022+18%3A53%3A43+GMT-0400+(%E5%8C%97%E7%BE%8E%E4%B8%9C%E9%83%A8%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __cf_bm=.fksdoBlzBs1zuhiY0rYFqFhDkstwwQJultZ756_yrw-1647645226-0-AaluVZQHZhOL5X4GXWxqEIC5Rp3/gkhKORy7WXjZpp5N/a4ovPxRX6KUxD/zpjZ/YFHBokF82hLwBtxtwetYhp/TSrGowLS7sC4nnLNy2WWMpZSA7Fv1tMISsR6qBZdPvg==; locale=en-US",
            "origin":"https://discord.com",
            "referer":"https://discord.com/register",
            "sec-ch-ua" : "Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99",
            "sec-ch-ua-mobile":"?0",
            "sec-ch-ua-platform":"macOS",
            "sec-fetch-dest":"empty",
            "sec-fetch-mode":"cors",
            "sec-fetch-site":"same-origin",
            "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
            "x-discord-locale": "en-US",
            "x-fingerprint": fingerprint,
            "x-super-properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJ6aC1DTiIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85OS4wLjQ4NDQuNzQgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijk5LjAuNDg0NC43NCIsIm9zX3ZlcnNpb24iOiIxMC4xNS43IiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjExOTc2MSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
        }

        resp = requests.post("https://discord.com/api/v9/auth/register",json=param,headers=headers,proxies=self.Settings.get_proxy())

        token = None

        try:
            token = resp.json()['token']
        except Exception as e:
            self.Logger.error(__name__,"Cannot fetch token - "+resp.text)
            sys.exit(0)

        self.Logger.content(__name__, "Discord token: ", str(token))

        #self.Logger.info(__name__, "Verifing without proxy")
        core.PhoneNumberVerifier.Verify(
            ptoken           = Settings.onlinesimru,
            stoken           = Settings.capmonster,
            discord_token    = token,
            discord_password = password
            ).verify_phone_number()

        self.Logger.info(__name__,"finished verifying token phone number")


if __name__ == "__main__":
    Main()


