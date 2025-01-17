# -*- coding: utf-8 -*-
"""Portscanner.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rkGttQhPZ754aYLLzHCw1outWBaPb1QA
"""

import socket
import termcolor

def scan(target, ports):
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ipaddress, port):
    try:
         sock=socket.socket()
         sock.connect((ipaddress, port))
         print("[+] Port Opened " + str(port))
         sock.close()
    except:
           print("[-] Port Closed " + str(port))

targets=input("Enter Targets To scan(split them by ,): ")
ports=int(input("Enter Ports To Scan: "))
if ',' in targets:
         print("[*] Scanning Multiple Targets")
         for ip_addr in targets.split(','):
              scan(ip_addr.strip(' '), ports)
else:
         scan(targets, ports)