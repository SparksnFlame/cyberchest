#!/bin/python3

#Needs debugging and input validation

import sys
import socket
from datetime import datetime

print("-" * 50)
print("Scanner started")
#Define target
target = input("Please insert valid IP to scan:" )

#Validate IP provided
#if len(sys.argv) == 2:

#else:
#    print("Invalid amount of arguments")
#    print("Syntax: python3 scanner.py <IP>")
#    sys.exit()
    
#Add a banner
print("-" * 50)
print("Scanning target: " + target)
dt_i = datetime.now()
print("Time started: " + str(dt_i))
print("-" * 50)

#Execute scan
try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #Error indicator of socket function
        #Print results
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        s.close()
    #Print final statistcs and banner
    dt_f = datetime.now()
    print("Time ended: " + str(dt_f))
    time_elapsed = dt_f - dt_i
    print(f"Time elapsed: {time_elapsed}")
    print("-" * 50)

except KeyboardInterrupt:
    print("\nExiting scanner")
    sys.exit()
except socket.gaierror:
    print("Hostname cannot be resolved")
    sys.exit()
except socket.error:
    print("Could not connect to server")
    sys.exit()
