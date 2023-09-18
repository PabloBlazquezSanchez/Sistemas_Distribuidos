#!/usr/bin/python3

import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b"Hello World", ("127.0.0.1", 1234))
    s.close()