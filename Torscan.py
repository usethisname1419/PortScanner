import socket
import sys
import requests
import socks
from datetime import datetime
from colorama import init, Fore, Style
import subprocess

init(autoreset=True)
subprocess.call('clear', shell=True)

print(Style.BRIGHT + Fore.YELLOW + "START AT:", (datetime.now()))
print("=============COREXITAL PORT SCANNER=============")
print("")
target = input("Enter IP Address:  ")
hack = socket.gethostbyname(target)

def connect_to_socks():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050, True)
    socket.socket = socks.socksocket




print("Scanning IP", hack)
print("Starting to get target information at: ")

t1 = datetime.now()
print(t1)
print("LOADING...")
r = requests.get('http://wtfismyip.com/text')
print(Style.BRIGHT + Fore.BLUE + "CURRENT IP:", r.text) #prints my ordinary IP address
print("")
print("CONNECTING SOCKS....")
def starthack():



    try:
        port = 22
        connect_to_socks()
        r = requests.get('http://wtfismyip.com/text')
        print(Style.BRIGHT + Fore.BLUE + "CONNECTED VIA:", r.text)
        hacking = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hacking.settimeout(20)
        result = hacking.connect((hack, port))
        if result == 0:
            print("PORT:", port, Style.BRIGHT + Fore.GREEN + "    OPEN")
            hacking.close()
            if r.status_code == 200:
                print(Style.BRIGHT + Fore.YELLOW + "STATUS:", Style.BRIGHT + Fore.GREEN + "OK")
            else:
                print(Style.BRIGHT + Fore.YELLOW + "STATUS:", Style.BRIGHT + Fore.RED + "BAD")
            print(datetime.now())

        else:
            print("PORT:", port, Style.BRIGHT + Fore.RED + "    CLOSED")
            hacking.close()
            if r.status_code == 200:
                print(Style.BRIGHT + Fore.YELLOW + "STATUS:", Style.BRIGHT + Fore.GREEN + "OK")
            else:
                print(Style.BRIGHT + Fore.YELLOW + "STATUS:", Style.BRIGHT + Fore.RED + "BAD")
            print(datetime.now())

    except KeyboardInterrupt:
        print(t1)
        print("Canceled")
        sys.exit()

    except socket.gaierror:
        print(t1)
        print("Hostname could not be resolved. Exiting")
        sys.exit()
    except socket.error:
        print(t1)
        print("Error")
        print("ERROR")
        sys.exit()

starthack()

print("")
print(Style.BRIGHT + Fore.YELLOW + "END OF REPORT")
print("2023 - Corexital")
