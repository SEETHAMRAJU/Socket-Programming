from socket import *
sock = socket(AF_INET,SOCK_DGRAM)
IP = "127.0.0.1"
PORT = 890
MES = "Hi , How are you?"
sock.sendto(MES,(IP,PORT))

