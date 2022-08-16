import socket
port = 3000
CHUNK = 35535

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Host_Name = '127.0.0.1'

while True:
    soc.connect((Host_Name, port))
    message = input('Client: ')
    data = message.encode('ascii')
    soc.send(data)
    data = soc.recv(CHUNK)
    text = data.decode('ascii')
    print(f'Server: {text}')
