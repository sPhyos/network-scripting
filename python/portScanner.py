#!/usr/bin/python3
# scanner.py

import socket
import time

def is_pronic(n):
    x = int((n)**0.5)
    return x * (x + 1) == n

startTime = time.time()

target = input('Please specify the host that you want to scan: ')
target_IP = socket.gethostbyname(target)
print('Initiating Scan for host:', target_IP)

for i in range(4000, 5001):
    if is_pronic(i):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = scanner.connect_ex((target_IP, i))
        if(conn == 0):
            print('Port %d: OPEN' % (i))
        scanner.close()

endTime = time.time()
totalTime = endTime - startTime
print('Total Time: %s' % (totalTime))
