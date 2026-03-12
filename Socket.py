# Networking is the process of connecting two or more computers or devices so that they can share data, resources, and communicate with each other. It allows devices to send and receive information, like files, emails, or access the internet.

# Types of Network

# 1.LAN(Local Area Network)-->Small area, like a home or office.
# 2.WAN(Wide Area Network)-->Large area, like cities or countries.
# 3.MAN(Metropolitan Area  Network)-->Covers a city.
# 4.PAN(Personal Area Network)-->Very small area, usually a person.

# Protocols -->Rules for communication between devices.

# 1.TCP/IP: Standard for internet communication.
# 2.HTTP/HTTPS: For web communication.
# 3.FTP: For file transfer

# Networking Media:

# 1.Wired: Ethernet cables

# 2.Wireless: Wi-Fi, Bluetooth, satellite.

import socket

host = "localhost"
port = 5001 
server = socket.socket()
server.bind((host,port))
server.listen()
conn12, addr1 = server.accept()
print ("Connection from: " + str(addr1))
while True:
   data = conn12.recv(2000).decode()
   if not data:
      break
   data = str(data).upper()
   print (" from client: " + str(data))
   data = input("type message: ")
   conn12.send(data.encode())
conn12.close()   