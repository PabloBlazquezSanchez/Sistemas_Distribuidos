import socket
import struct
import random

words = ["Hola Mundo", "struct", "lsh", "ñandú"]
palabra = random.choice(words).encode()
length = len(palabra)
formato = f'!h{str(length)}s'


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    data = struct.pack(formato, len(palabra), palabra)
    s.sendto(data, ("localhost", 8080))