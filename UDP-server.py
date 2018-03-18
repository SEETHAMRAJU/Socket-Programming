# UDP SERVER Program 
import socket
client_address = ("172.16.82.242",9476)                                 #Client Address
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)                  
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)                #For re 
sock.bind(client_address)
x = []
count = 0
y = 1
while 1:
    while y: #Infiniteloop
          data,address = sock.recvfrom(1024)
          x.append(int(data))
          count += 1
          if(count == 5):
              y = 0
    x.sort()
    sock.sendto(str(x),address)
    print x
    break










#172.16.82.242
"""
#sorting from here 
    while(data>0):
        d,address = sock.recvfrom(8)
        a.append(d)
        data -= 1
    a.sort()
    print a
    X = 0
"""    
    
