from colorama import Fore
from datetime import datetime
import time
class Logger:
    def info(self,name,msg):
        date_time = datetime.fromtimestamp(time.time())
        print(f"[{name} {date_time.strftime('%H:%M:%S')} {Fore.GREEN}INFO{Fore.RESET}] {msg}")

    def content(self,name,msg,content):
        date_time = datetime.fromtimestamp(time.time())
        print(f"[{name} {date_time.strftime('%H:%M:%S')} {Fore.CYAN}CONTENT{Fore.RESET}] {msg} {Fore.MAGENTA}{content}{Fore.RESET}")

    def warn(self,name,msg):
        date_time = datetime.fromtimestamp(time.time())
        print(f"[{name} {date_time.strftime('%H:%M:%S')} {Fore.YELLOW}WARNING{Fore.RESET}] {msg}")

    def error(self,name,msg):
        date_time = datetime.fromtimestamp(time.time())
        print(f"[{name} {date_time.strftime('%H:%M:%S')} {Fore.RED}ERROR{Fore.RESET}] {msg}")
