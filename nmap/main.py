#Import libraies

import pyfiglet #fancy banner, delete if pip and environment not installed
import sys #handling exceptions
import socket #port internet
from datetime import datetime #print in banner

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

target = input(str("Target IP: "))

#Banner
print("_" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

try:

    #Scan every port on the target ip
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #Return open port
        results = s.connect_ex((target,port))
        if results == 0:
            print("[*] Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting program.")
    sys.exit()

except socket.error:
    print("\n Host not found.")
    sys.exit()

    


