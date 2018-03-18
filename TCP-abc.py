import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address = ("127.0.1.1",9125)
client.connect(address)
