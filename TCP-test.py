import socket
import sys
import pickle
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
address = ("172.16.81.152",8080)
server.bind(address)
server.listen(10)
print "listening"
client,addr = server.accept()
print "Connection from",addr[0],":",addr[1]
while(1):
    Data = client.recv(1024)
    #data = pickle.loads(Data)
    print "Recieved: ",Data
    #numbers = map(int,data.split())
    #numbers.sort()
    #ans = ""
    #for x in numbers:
    #    ans += str(x)+" "
    #Ans =
    #reply = pickle.dump("NM")
    client.send("NM")
    if(data == "close"):
        client.send("Disconnecting")
        client.close()
        break
