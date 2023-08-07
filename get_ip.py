# get_ip.py

import socket

def get_server_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        IPAddr = s.getsockname()[0]
        s.close()
    except:
        IPAddr = input("Couldn't determine the default interface. Please enter the IP address of the network interface: ")
    return IPAddr

