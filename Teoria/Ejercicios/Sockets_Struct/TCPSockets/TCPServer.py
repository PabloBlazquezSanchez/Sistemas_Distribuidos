import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 12345

sock.bind((host, port))

sock.listen(5)

conn, addr = sock.accept()

data = conn.recv(1024)

print("Received message:", data.decode())
print("From address:", addr)

conn.send("OK".encode())

conn.close()