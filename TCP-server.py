import socket
from random import *
host = ("172.16.82.242",9476)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("172.16.82.242",9476))
s.listen(5)
connection,address = s.accept()
print "Address = ",address
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
