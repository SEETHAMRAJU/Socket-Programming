####         TCP -Client Program for sending 5 numbers ########

import socket
import random
port = random.randint(5000,9000)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       #Creating a socket
address = ("172.16.81.152",9272)
i =0
client.connect(address)                                         #Connecting to a server of desired choice
while 1: 
    i = 0 
    P = ""          #For sending the given numbers in the form of string
    while(i<5):                                     
        P = P + str(random.randint(1,10)) + " "         #Generating Random numbers
        i += 1
    print "P before : " + P 
    i = 0
    client.send(P)                  #Sending the data
    print "Data Sent"
    data = client.recv(1024)        #Recieving data from the server 
    print data                      #Printing the server
    break;    

