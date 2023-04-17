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
############# Import Modules. Modules are installed by using " pip install (pkname)"###############
#############Modules are other pieces if code available with python. very helpful to sav time##########
target = input("Enter IP Address:  ")

with open('proxyf.txt', 'r') as f:
    proxy = f.read().splitlines()
proxies = {
    'http': (proxy,)
}



############## Saving input value as a variable####################
hack = socket.gethostbyname(target)

print("Scanning IP", hack)
print("Starting to get target information at: ")


###################You can prin a variable or plain text###########3
t1 = datetime.now()
print(t1)
##############We use the modules datime to print the current time#################
print("LOADING...")
print("")


def starthack():
######################### Fuctions: def means Define. functions are called with the () characters##############
    try:
        for port in range(1, 100):
            r = requests.get(url='https://google.com', proxies=proxies)
            hacking = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            hacking.settimeout(10)
            result = hacking.connect_ex((hack, port))
            if result ==0:
                print("PORT:", port, Style.BRIGHT + Fore.GREEN + "    OPEN")
                hacking.close()
                print(Style.BRIGHT + Fore.YELLOW + "STATUS:", r.status_code)
                print(datetime.now())
                
            else:
                print("PORT:", port, Style.BRIGHT + Fore.RED +"    CLOSED")
                hacking.close()
                print(Style.BRIGHT + Fore.YELLOW + "STATUS:", r.status_code)
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

###########Calling a fuction##################33
print("")
print(Style.BRIGHT + Fore.YELLOW + "END OF REPORT")
print("2023 - Corexital")
