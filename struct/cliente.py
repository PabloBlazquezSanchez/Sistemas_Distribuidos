import socket
import struct
import random

msd = "Pablo.Blazquez1@alu.uclm.es"
l = 

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
        s.sendto(b"Pablo.Blazquez1@alu.uclm.es", ("192.168.88.252", 4080))
        print("El mensaje fue enviado")
        # s.close()
    # s.sendto(b"Esto es una prueba de UDP", ("192.168.88.252", 4080))
    # print("El mensaje fue enviado")
    # s.close()