#!/usr/bin/env python
import socket

target_host = "www.google.com"
target_port = 80

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
# c.sendall(output.encode('utf-8'))
# In python 3, strings are unicode but socket conns expect byte strings
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = client.recv(4096)
print(response)
