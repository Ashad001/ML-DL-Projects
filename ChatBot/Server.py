import socket

port = 3000
CHUNK = 65535 # Recieve at most these number of bytes at once

# Create a socket object (that will connect us to internet)
# Syntax: socket.socket(Family, type)
# AF_NET: Family of ipv4 32-bit ip addresses
# SOCK_DGRAM: UDP (google it!!) Overview: data can be loss
# SOCK_STREAM: For TCP applications
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# We need some IP address that the server will listen to when the message will come.
HostName = '127.0.0.1'   # IP address of local machine ... Same for everyone
soc.bind((HostName, port))   # Bind the socket with the local machine and on port 3000
# So if message comes on this address then the server could read!!!

# Run this server infinitely till I stop it manually
while True:
    data, clientAdd = soc.recvfrom(CHUNK)
    message = data.decode('ascii')  # As data travels in byte so we have to convert it into ascii
    print(f'Client: {message}')
    message_sent = input("Server: ")
    data = message_sent.encode('ascii')
    # Now just send the data to IP add that sent the data
    soc.sendto(data,clientAdd)
    
