import socket

target_host = "www.google.com"
target_port = 80

# Create a socket client 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client 
client.connect((target_host, target_port))

# Send some data 
client.send(b'GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n')

# receive some data
response = client.recv(4096) asd

print(response)
