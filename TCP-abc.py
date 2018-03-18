#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import random
import pickle
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
portl = random.randint(1600,9978)# Reserve a port for your service.
port = 9976
s.connect((host, port))
while 1:
    
    s.send()
    data = s.recv(1024)
    D = pickle.loads(data)
    print D
    s.close()                     # Close the socket when done
