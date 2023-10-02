#!/usr/bin/python3 -u

'''
Pablo Blázquez Sánchez
'''
"Usage: {0} <host> <port>"

import sys
import socket
import struct


server_addr = (sys.argv[1], int(sys.argv[2]))


def deserialize_reading(data):
    # FIXME: complete this function for data unmarshalling

    # Your code here

    l = struct.calcsize(data)

    color, hour, minute, second = struct.unpack('!' + str(l) + 's', data[2:])



    return color, hour, minute, second


if len(sys.argv) != 3:
    print(__doc__.format(__file__))
    sys.exit(1)

# FIXME: write your own UCLM ID
uclm_id = 'Pablo.Blazquez1@alu.uclm.es'  # if your email is John.Doe@alu.uclm.es

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Sending UCLM ID...')
msg = 'UID'.encode() + uclm_id.encode()
sock.sendto(msg, server_addr)

msg = sock.recv(1024)
print(msg.decode())
reading = deserialize_reading(msg)

print('Sending result...')


# FIXME: send the result and print the server response

print(sock.recv(1024).decode())

sock.close()
