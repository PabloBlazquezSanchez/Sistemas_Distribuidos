import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = ''
port = 12345

sock.bind((host, port))

data, addr = sock.recvfrom(1024)

print("Received message:", data.decode())
print("From address:", addr)

sock.sendto("OK".encode(), addr)

sock.close()