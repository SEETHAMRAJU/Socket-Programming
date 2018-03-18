import socket
host = ("127.0.0.1",9867)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock
sock.bind(host)
sock.listen(5)
while(1):
    clnt,addr = sock.accept()
    client.sendall("SUP")
    #data = client.recv(1024)
    #print data
sock.close()
