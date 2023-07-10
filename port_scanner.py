import sys
import socket
from datetime import datetime

target = input(str("Target IP: "))
scan_type = input(str("Enter 'tcp' for TCP ports or 'udp' for UDP ports: "))
print("-------------------------")
print("Scanning " + target)
print("Scanning type: " + scan_type)
print("Scanning started at: " + str(datetime.now()))
print("-------------------------")

try:
    if scan_type == "tcp":
        protocol = socket.SOCK_STREAM
    elif scan_type == "udp":
        protocol = socket.SOCK_DGRAM
    else:
        print("Invalid scan type. Please enter 'tcp' or 'udp'")
        sys.exit()

    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, protocol)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target, port))
        if result == 0:
            print("[+] Port " + str(port) + " is open")

        s.close()

except KeyboardInterrupt:
    print("\nExiting")
    sys.exit()

except socket.error:
    print("\nHost unresponsive")
    sys.exit()
