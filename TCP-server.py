import socket
from random import *
import socket
from random import *
port = randint(5000,9000)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("",8559))
s.listen(1)
connection,address = s.accept()
P =[]
while(1):
    i = 0
    #while(i<5):
    #    d = s.recv(1024)
    #    P.append(int(d))
    #    i += 1
    d = connection.recv(1024)
    d = map(int , d.split())
    d.sort()       
    i = 0
    print d
    connection.send(str(d))
    connection.close()    
    print "Connection Closed"
    break
