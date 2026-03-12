
import socket

host = "localhost"
port = 5001
obj = socket.socket()
obj.connect((host,port))
message = input("type message: ")
while message != 'q':
   obj.send(message.encode())
   data = obj.recv(2000).decode()
   print ('Received from server: ' + data)
   message = input("type message: ")
obj.close()