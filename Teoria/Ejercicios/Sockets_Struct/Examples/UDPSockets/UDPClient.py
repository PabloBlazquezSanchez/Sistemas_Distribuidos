import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = ''
port = 12345

message = 'Hello'.encode()

try:
    sent = sock.sendto(message, (host, port))
    data, _ = sock.recvfrom(4096)
    print("Received:", data.decode())
finally:
    sock.close()