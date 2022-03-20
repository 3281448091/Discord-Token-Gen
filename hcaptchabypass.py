from datetime import date, datetime
import math
import base64
import httpx
import urllib
import hashlib
from json import dumps
import json
import os
import random

headers = {
    "Host": "hcaptcha.com",
    "Connection": "keep-alive",
    "sec-ch-ua": 'Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92',
    "Accept": "application/json",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Content-type": "application/json; charset=utf-8",
    "Origin": "https://newassets.hcaptcha.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://newassets.hcaptcha.com/",
    "Accept-Language": "en-US,en;q=0.9"

}

def N_Data(req) -> str:
        try:
            """
            this part takes the req value inside the getsiteconfig and converts it into our hash, we need this for the final step.
            (thanks to h0nde for this function btw, you can find the original code for this at the top of the file.)
            """
            x = "0123456789/:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

            req = req.split(".")

            req = {
                "header": json.loads(
                    base64.b64decode(
                        req[0] +
                        "=======").decode("utf-8")),
                "payload": json.loads(
                    base64.b64decode(
                        req[1] +
                        "=======").decode("utf-8")),
                "raw": {
                    "header": req[0],
                    "payload": req[1],
                    "signature": req[2]}}

            def a(r):
                for t in range(len(r) - 1, -1, -1):
                    if r[t] < len(x) - 1:
                        r[t] += 1
                        return True
                    r[t] = 0
                return False

            def i(r):
                t = ""
                for n in range(len(r)):
                    t += x[r[n]]
                return t

            def o(r, e):
                n = e
                hashed = hashlib.sha1(e.encode())
                o = hashed.hexdigest()
                t = hashed.digest()
                e = None
                n = -1
                o = []
                for n in range(n + 1, 8 * len(t)):
                    e = t[math.floor(n / 8)] >> n % 8 & 1
                    o.append(e)
                a = o[:r]

                def index2(x, y):
                    if y in x:
                        return x.index(y)
                    return -1
                return 0 == a[0] and index2(a, 1) >= r - 1 or -1 == index2(a, 1)

            def get():
                for e in range(25):
                    n = [0 for i in range(e)]
                    while a(n):
                        u = req["payload"]["d"] + "::" + i(n)
                        if o(req["payload"]["s"], u):
                            return i(n)

            result = get()
            hsl = ":".join([
                "1",
                str(req["payload"]["s"]),
                datetime.now().isoformat()[:19]
                .replace("T", "")
                .replace("-", "")
                .replace(":", ""),
                req["payload"]["d"],
                "",
                result
            ])
            return hsl
        except Exception as e:
            print(e)
            return False

def REQ_Data(host, sitekey,proxy):
        try:
            r = httpx.get(f"https://hcaptcha.com/checksiteconfig?host={host}&sitekey={sitekey}&sc=1&swa=1", headers=headers,proxies={"https://": f"http://{proxy}"},timeout=4)
            if r.json()["pass"]:
                return r.json()["c"]
            else:
                return False
        except :
            return False

def Get_Captcha(host, sitekey, n, req,proxy):
        try:
            json = {
                "sitekey": sitekey,
                "v": "b1129b9",
                "host": host,
                "n": n,
                'motiondata': '{"st":1628923867722,"mm":[[203,16,1628923874730],[155,42,1628923874753],[137,53,1628923874770],[122,62,1628923874793],[120,62,1628923875020],[107,62,1628923875042],[100,61,1628923875058],[93,60,1628923875074],[89,59,1628923875090],[88,59,1628923875106],[87,59,1628923875131],[87,59,1628923875155],[84,56,1628923875171],[76,51,1628923875187],[70,47,1628923875203],[65,44,1628923875219],[63,42,1628923875235],[62,41,1628923875251],[61,41,1628923875307],[58,39,1628923875324],[54,38,1628923875340],[49,36,1628923875363],[44,36,1628923875380],[41,35,1628923875396],[40,35,1628923875412],[38,35,1628923875428],[38,35,1628923875444],[37,35,1628923875460],[37,35,1628923875476],[37,35,1628923875492]],"mm-mp":13.05084745762712,"md":[[37,35,1628923875529]],"md-mp":0,"mu":[[37,35,1628923875586]],"mu-mp":0,"v":1,"topLevel":{"st":1628923867123,"sc":{"availWidth":1680,"availHeight":932,"width":1680,"height":1050,"colorDepth":30,"pixelDepth":30,"availLeft":0,"availTop":23},"nv":{"vendorSub":"","productSub":"20030107","vendor":"Google Inc.","maxTouchPoints":0,"userActivation":{},"doNotTrack":null,"geolocation":{},"connection":{},"webkitTemporaryStorage":{},"webkitPersistentStorage":{},"hardwareConcurrency":12,"cookieEnabled":true,"appCodeName":"Mozilla","appName":"Netscape","appVersion":"5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36","platform":"MacIntel","product":"Gecko","userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36","language":"en-US","languages":["en-US","en"],"onLine":true,"webdriver":false,"serial":{},"scheduling":{},"xr":{},"mediaCapabilities":{},"permissions":{},"locks":{},"usb":{},"mediaSession":{},"clipboard":{},"credentials":{},"keyboard":{},"mediaDevices":{},"storage":{},"serviceWorker":{},"wakeLock":{},"deviceMemory":8,"hid":{},"presentation":{},"userAgentData":{},"bluetooth":{},"managed":{},"plugins":["internal-pdf-viewer","mhjfbmdgcfjbbpaeojofohoefgiehjai","internal-nacl-plugin"]},"dr":"https://discord.com/","inv":false,"exec":false,"wn":[[1463,731,2,1628923867124],[733,731,2,1628923871704]],"wn-mp":4580,"xy":[[0,0,1,1628923867125]],"xy-mp":0,"mm":[[1108,233,1628923867644],[1110,230,1628923867660],[1125,212,1628923867678],[1140,195,1628923867694],[1158,173,1628923867711],[1179,152,1628923867727],[1199,133,1628923867744],[1221,114,1628923867768],[1257,90,1628923867795],[1272,82,1628923867811],[1287,76,1628923867827],[1299,71,1628923867844],[1309,68,1628923867861],[1315,66,1628923867877],[1326,64,1628923867894],[1331,62,1628923867911],[1336,60,1628923867927],[1339,58,1628923867944],[1343,56,1628923867961],[1345,54,1628923867978],[1347,53,1628923867994],[1348,52,1628923868011],[1350,51,1628923868028],[1354,49,1628923868045],[1366,44,1628923868077],[1374,41,1628923868094],[1388,36,1628923868110],[1399,31,1628923868127],[1413,25,1628923868144],[1424,18,1628923868161],[1436,10,1628923868178],[1445,3,1628923868195],[995,502,1628923871369],[722,324,1628923874673],[625,356,1628923874689],[523,397,1628923874705],[457,425,1628923874721]],"mm-mp":164.7674418604651},"session":[],"widgetList":["0a1l5c3yudk4"],"widgetId":"0a1l5c3yudk4","href":"https://discord.com/register","prev":{"escaped":false,"passed":false,"expiredChallenge":false,"expiredResponse":false}}',
                "hl": "en",
                "c": dumps(req)
            }

            data = urllib.parse.urlencode(json)
            headers = {
                "Host": "hcaptcha.com",
                "Connection": "keep-alive",
                "sec-ch-ua": 'Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92',
                "Accept": "application/json",
                "sec-ch-ua-mobile": "?0",
                "Content-length": str(len(data)),
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
                "Content-type": "application/x-www-form-urlencoded",
                "Origin": "https://newassets.hcaptcha.com",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://newassets.hcaptcha.com/",
                "Accept-Language": "en-US,en;q=0.9"

            }

            cookies = {"hc_accessibility": "wAHi1MOKSosBLK6HVeeBzfbaQknsYZOOkIB/s3TXYK3NzxiIzJ3HzV6uQOMlyTSI1GIVz9AazrmLIgl7NAufVofFaQDhnTL9CNyhqVwlaibJmi6mQrr377HrCaTI7VCWxo1kniMjJDOEz4X29+NH5awd4jH6hPyKIOZhNjWuMrNSKu6ZFLuRSgOiy4c+0idoOSRYiOiX9HK8KkQaHk8EfkR05vRrjPBkaNVKqg1RcpcfREQ06gIS9YzkItTt+2z/aHHZU1rAdJTyJ8oijsq2Mis23zqp9EWQ52H4oWEstionkOct9Z8NgybESmrdNsowi3NXNOoVwWoU4ZEwGCbjG8eO+2HnSP1vPKUi6tT7Z39E2eCMAJJDn9dyenkOuFRcOMmFiMIIIFsTUniyM7EhvSWxWDFvI+4zbx/+TP5pQClZJcLbXinpw1SMk3GVT3S6EG2n/DyLQ0/p3+/CJYbr7sVjdeRLQBGyCMvaOPy+dvaRH+mszz58EoV35sq9835SPRD17jNym9E=UCa12gEu9VIPScd9"}
            r = httpx.post(f"https://hcaptcha.com/getcaptcha?s={sitekey}",cookies=cookies, data=data, headers=headers, timeout=4,proxies={"https://": f"http://{proxy}"})

            return r.json()
        except Exception as e:
            print(e)
            return False

def bypass(sitekey, host,proxy):
    try :
        req = REQ_Data(sitekey=sitekey, host=host,proxy=proxy)
        req["type"] = "hsl"
        n = N_Data(req["req"])
        res = Get_Captcha(sitekey=sitekey, host=host,proxy=proxy,n=n, req=req)
        if "generated_pass_UUID" in res:
            captcha = res["generated_pass_UUID"]
            return captcha
        else:
            return False
    except : return False
