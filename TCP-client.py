####         TCP -Client Program for sending 5 numbers      ########
"""
SEETHAMRAJU PURVAJ - IMT2017039 TCP - Client

RAVI KIRAN - IMT2017034 TCP - Server
"""
"""
Description :
    We send 5 randomly generated numbers in a string separated by spaces and then we receive the sorted sequence of numbers.
"""
import socket
import random
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)                 #Creating a socket
address = ("172.16.81.152",9272)
i =0
client.connect(address)                                                 #Connecting to a server of desired choice
while 1: 
    i = 0 
    P = ""                                                              #For sending the given numbers in the form of string
    while(i<5):                                     
        P = P + str(random.randint(1,10)) + " "                         #Generating Random numbers
        i += 1
    print "P before : " + P 
    i = 0
    client.send(P)                                                      #Sending the data
    print "Data Sent"
    data = client.recv(1024)                                            #Recieving data from the server 
    print data                                                          #Printing the server
    break;                                                              #Stopping the loop after one iteration 

