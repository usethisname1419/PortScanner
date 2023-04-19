import socket
import sys
import requests
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

proxy = {
    'http':  'socks5://localhost:9050',
    'https': 'socks5://localhost:9050',
}


print("Starting at: ")

t1 = datetime.now()
print(t1)
print("LOADING...")
r = requests.get('http://wtfismyip.com/text')
print(Style.BRIGHT + Fore.BLUE + "CURRENT IP:", r.text) #prints my ordinary IP address
print("")
print(Style.BRIGHT + Fore.YELLOW + "CONNECTING TOR....")
print("")
r = requests.get('http://wtfismyip.com/text', proxies=proxy)
print(Style.BRIGHT + Fore.BLUE + "CONNECTED VIA:", r.text)
if r.status_code == 200:
    print(Style.BRIGHT + Fore.YELLOW + "PROXY STATUS:", Style.BRIGHT + Fore.GREEN + "OK")
else:
    print(Style.BRIGHT + Fore.YELLOW + "PROXY STATUS:", Style.BRIGHT + Fore.RED + "BAD")
print("")
print("STARTING PROCESS.....")
def starthack(num):
######################### Fuctions: def means Define. functions are called with the () characters##############
    try:
        for port in range(1, 100):
            hacking = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            hacking.settimeout(10)
            result = hacking.connect_ex((hack, port))
            if result ==0:
                print(Style.BRIGHT + Fore.YELLOW + "PORT:", port, Style.BRIGHT + Fore.GREEN + "    OPEN")
                hacking.close()
                print(datetime.now())

            else:
                print(Style.BRIGHT + Fore.YELLOW + "PORT:", port, Style.BRIGHT + Fore.RED +"    CLOSED")
                hacking.close()
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
starthack(20)

print("")
print(Style.BRIGHT + Fore.YELLOW + "END OF REPORT")
print("2023 - Corexital")
