#!/usr/bin/python3
# networkingClientSocket.py

import socket

# Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the host and port
host = "192.168.0.191"
port = 8080

# Connect to the server
client.connect((host, port))

# Receive data
msg = client.recv(1024)

# Close the connection
client.close()

# Print the received message
print(msg)

