import socket               # Import socket module
import random
import pickle
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
portl = random.randint(1600,9978)                # Reserve a port for your service.
s.bind((host, 9976))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   x = pickle.dumps("SUP")
   c.send(x)
   #print 'Recieved : '+str(c)
   #c.send('Thank you for connecting')
   c.close()                # Close the connection
