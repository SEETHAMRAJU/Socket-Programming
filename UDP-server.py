from socket import *
client_address = ()
sock = socket(AF_INET,SOCK_DGRAM)
sock.bind(client_address)
X = 1
count = 0
a =[]
while X:
    data,address = sock.recvfrom(8)
    while(data>0):
        d,address = sock.recvfrom(8)
        a.append(d)
        data -= 1
    a.sort()
    print a
    X = 0
    
    
