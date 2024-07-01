#!/usr/bin/python3
# server.py

import socket

# Create a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the host and define the port
host = ""
port = 8080

# Bind the server to the port
server.bind((host, port))

# Start listening for connections
server.listen(5)
print("Server listening on port", port)

while True:
    # Accept a connection
    client_socket, addr = server.accept()
    print("Connection from", addr)
    
    # Send a message to the client
    msg = ""
    client_socket.send(msg.encode('ascii'))
    
    # Close the client connection
    client_socket.close()
