# This is a basic TCP scanner using socket

import socket  # It is used to let python talk to other computers on a network, used for connecting websites,servers, etc
import threading  # scans many ports at once

target = input("Enter target IP :  ")


def scan(port):
    # Creates a new socket then IPV4 addressing and TCP protocol
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)  # Maximum wait time for connection attempt
    if s.connect_ex((target, port)) == 0:
        print(f"[+] Port {port} is OPEN")

    s.close()


print(f"Scanning {target}   \n")

for port in range(1, 1025):
    thread = threading.Thread(target=scan, args=(port,))
    thread.start()
