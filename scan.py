import socket
import sys
from datetime import datetime

############# Import Modules. Modules are installed by using " pip install (pkname)"###############
#############Modules are other pieces if code available with python. very helpful to sav time##########
target = input("enter ip address:  ")

############## Saving input value as a variable####################
hack = socket.gethostbyname(target)

print(hack)
print("Starting to get target information at: ")
###################You can prin a variable or plain text###########3
t1 = datetime.now()
print(t1)
##############We use the modules datime to print the current time#################

def starthack():
######################### Fuctions: def means Define. functions are called with the () characters##############
    try:
        for port in range(1, 100):
####################### This is a loop, targeting all ports in that range.####################
            hacking = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            hacking.settimeout(10)
            result = hacking.connect_ex((hack, port))
            if result ==0:
                print("PORT:", port,"    OPEN")
                hacking.close()
                print(t1)
            else:
                print("PORT:", port, "    CLOSED")
                hacking.close()
                print(t1)
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

print("END OF REPORT")
print("Corexital")
