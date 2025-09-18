import socket
import struct

host = ''
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((host,port))
    while True:
        data, addr = sock.recvfrom(1024)

        i1, i2 = struct.unpack('!ii', data)

        sum_result = i1 + i2

        to_send = struct.pack('!i', sum_result)
        
        sock.sendto(to_send, addr)