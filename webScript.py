import socket
import requests

url = "http://www.offensive-security.com"

remote_host = "www.offensive-security.com"
remote_port = 80
request = "GET / HTTP/1.1\r\nHost: www.offensive-security.com\r\n\r\n"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((remote_host,remote_port))
client.send(request.encode())

response = client.recv(4096)
print(response.decode())

response = requests.get(url)
print(response.content.decode())