import socket

server_ip ="10.114.245.220"  # Example: 192.168.43.150
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, port))
server.listen(1)

print("Waiting for client...")
conn, addr = server.accept()
print("Connected with:", addr)

while True:

    reply = conn.recv(1024).decode()
    if not reply:
      break
    print("Client:", reply)
    msg = input("You: ")
    conn.send(msg.encode())

conn.close()
    
