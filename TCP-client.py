import socket
import random
port = random.randint(5000,9000)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address = ("",8559)
i =0 
P = ""
print "HI"
while(i<5):
    P = P + str(random.randint(1,10)) + " "
    i += 1
print "P prepared"
print "P before : " + P
client.connect(address)
#while 1:
i = 0
    #while(i<5):
    #    p = random.randint(1,10)
    #    client.send(str(p))
    #    i += 1
print 'Connected'
client.send(P)
print "Data Sent"
data = client.recv(1024)
print data


