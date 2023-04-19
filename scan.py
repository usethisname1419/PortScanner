import socket
import sys
import requests
import socks
import threading
from queue import Queue
import time
from datetime import datetime
from colorama import init, Fore, Style
import subprocess

init(autoreset=True)
subprocess.call('clear', shell=True)



print(Style.BRIGHT + Fore.YELLOW + "START AT:", (datetime.now()))
print("=============COREXITAL PORT SCANNER=============")
print("")
target = input("ENTER TARGET IP:  ")
ports = input("ENTER NUMBER OF PORTS TO SCAN:   ")
threads = input("ENTER NUMBER OF THREADS:   ")
hack = socket.gethostbyname(target)
thr = int(threads)
todo = input("USE TOR? Y/N:   ")

if todo =="Y":
    r = requests.get('http://wtfismyip.com/text')
    print(Style.BRIGHT + Fore.BLUE + "CURRENT IP:", r.text)  # prints my ordinary IP address
    print("CONNECTING TO TOR.....")
    socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9050)
    socket.socket = socks.socksocket
    r = requests.get('http://wtfismyip.com/text')
    print(Style.BRIGHT + Fore.BLUE + "CONNECTED VIA:", r.text)
    if r.status_code == 200:
        print(Style.BRIGHT + Fore.YELLOW + "PROXY STATUS:", Style.BRIGHT + Fore.GREEN + "OK")
    else:
        print(Style.BRIGHT + Fore.YELLOW + "PROXY STATUS:", Style.BRIGHT + Fore.RED + "BAD")
if todo =="N":
    r = requests.get('http://wtfismyip.com/text')
    print(Style.BRIGHT + Fore.BLUE + "CURRENT IP:", r.text)
    print(Style.BRIGHT + Fore.RED + "NOT CONNECTED TO TOR!!")
num = int(ports)
print("Starting at: ")

t1 = datetime.now()
print(t1)
print("LOADING...")


print("STARTING PROCESS.....")

def starthack(port):

        hacking = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hacking.settimeout(60)
        try:
            result = hacking.connect_ex((hack, port))
            if result ==0:
                service = socket.getservbyport(port)
                print(Style.BRIGHT + Fore.YELLOW + "PORT:", port, Style.BRIGHT + Fore.GREEN + "    OPEN")
                print("SERVICE:", service)
                hacking.close()
                print(datetime.now())
                print("")
                if port ==22:
                    print("SSH IS VULNERABLE!! ")


            else:
                print(Style.BRIGHT + Fore.YELLOW + "PORT:", port, Style.BRIGHT + Fore.RED +"    CLOSED")
                hacking.close()
                print(datetime.now())
                print("")

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


def threader():
    while True:
    
        worker = q.get()

       
        starthack(worker)

        q.task_done()


q = Queue()

for x in range(thr):
    t = threading.Thread(target=threader)


    t.daemon = True

    t.start()

start = time.time()


for worker in range(1, num):
    q.put(worker)


q.join()
print("")
print(Style.BRIGHT + Fore.YELLOW + "END OF REPORT")
print("2023 - Corexital")
