from socket import *
IP = "127.0.0.1"
PORT = 890
sock = socket(AF_INET,SOCK_DGRAM)
sock.bind((IP,PORT))
while(1):
    data, addr = sock.recvfrom(1024)
    print "message recieved!!"
    print data
