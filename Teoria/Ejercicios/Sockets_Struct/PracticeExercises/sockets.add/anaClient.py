import socket
import struct

host = ''
port = 12345

# Get values from terminal
import sys
addr = sys.argv[1]
num1 = int(sys.argv[2])
num2 = int(sys.argv[3])

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    serialized = struct.pack('!ii', num1, num2)
    sock.sendto(serialized, (addr.split(':')[0], int(addr.split(':')[1])))
    data = sock.recv(1024)

    result = struct.unpack('!i', data)[0]
    print(f"Result from server: {result}")