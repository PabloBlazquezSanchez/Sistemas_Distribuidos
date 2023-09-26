import socket
import sys
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            s.sendto("ñandú".encode(), ("127.0.0.1", 1234))
            print("Sent Message: Hello World")
        # sys.exit(0)