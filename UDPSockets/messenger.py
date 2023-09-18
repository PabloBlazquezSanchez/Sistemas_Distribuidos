#!/usr/bin/python3

import sys
import socket
import argparse

def client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"Hello World", ("127.0.0.1", 1234))
        print("Sent Message: Hello World")
        sys.exit(0)

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(('127.0.0.1', 1234))
        msg, addr = s.recvfrom(1024)
        s.close()
    print(msg.decode())

parser = argparse.ArgumentParser()
parser.add_argument(
    "-m",
    "--mode",
    type=str,
    default="server",
    required=False,
)
args = parser.parse_args()
server() if args.mode == "server" else client()