from portscan import *
import sys

ip = input("Desired IP> ")
module = Pscan(ip)

if module.validate_ipv4() == None:
    print("Invalid IP given!")
    sys.exit(0)

module.startScan()
print(module.getResponse())