import socket
import struct

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
host = ''
port = 12345
sock.bind((host, port))

# Listen for incoming messages
while True:
    data, addr = sock.recvfrom(1024)
    print("Received message:", struct.unpack('!ii', data))
    print("From address:", addr)

    # Parse the received message
    try:
        num1, num2 = struct.unpack('!ii', data)
        result = num1 + num2
        message = struct.pack('!i', result)
    except ValueError:
        message = struct.pack('!i', 0)

    # Send the result back to the client
    sock.sendto(message, addr)