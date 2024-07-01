# import socket 

# r_host = "www.megacorpone.com"
# r_port = 80

# request = f"GET / HTTP/1.1\r\nHost: {r_host}\r\n\r\n"

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((r_host,r_port))
# client.send(request.encode())

# respone = client.recv(4096)
# print(respone.decode())

import requests

url = "http://haad.uz:80"

res = requests.get(url)
print(res.content.decode())