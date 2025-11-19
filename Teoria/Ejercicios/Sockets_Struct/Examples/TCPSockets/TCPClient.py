import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 12345

message = 'Hello'.encode()

try:
    sock.connect((host, port))
    sock.send(message)
    data = sock.recv(1024)
    print("Received:", data.decode())
finally:
    sock.close()