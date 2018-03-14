import socket
from random import *
host = ("127.0.0.1",9476)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s.connect(host)
i = 0
P =[]
while(1):
    while(i<5):
        p = randint(1,10)
        P.append(p)
        s.sendto(str(p),host)
        i += 1
    print "Given array = "+str(P)
    data,addr = s.recvfrom(1024)
    print data
    break
