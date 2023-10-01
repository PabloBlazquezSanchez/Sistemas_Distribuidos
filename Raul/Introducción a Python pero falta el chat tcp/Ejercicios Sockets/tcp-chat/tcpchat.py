#!/usr/bin/python3
import socket
import _thread
import signal
import sys
import argparse
import struct


# En este caso, se va a desarrollar un chat entre cliente y servidor usando sockets TCP.
# Estos, a diferencia de los UDP, no se denotan como

#     socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# En su lugar, se escriben de la siguiente manera:

#     socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Además, podemos hacerlo en un sólo script, ya que al ser un chat en el que el cliente se alterna
# con el servidor, esperando uno a la espera del otro (bloqueándose), realmente se intercambian los
# roles, por lo que al final resultaría en código duplicado (no deseado)

# Entonces, lo haremos todo en una misma clase, y su uso se alternará a conveniencia (tal y como
# sucede en chats UDP de ejemplo)

class TCP_Messenger:
    '''Clase de la aplicación de mensajería TCP'''
    def __init__(self, host, port):
        # Constructor
        self.host = host
        self.port = port
        # Creamos el socket TCP (SOCK_STREAM) aquí, no en el main, ya que se ejecutarán instancias
        # de cliente y servidor directamente
        self.misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    