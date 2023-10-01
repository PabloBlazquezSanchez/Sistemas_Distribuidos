#!/usr/bin/python3
import socket
import sys
import argparse

class Messenger:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def exit_request(self, msg):
        return msg.lower() == 'exit'
    
    def enviar_mensaje(self):
        mensaje = input('Tú: ')
        self.s.send(mensaje.encode())
        if self.exit_request(mensaje): self.close()
    
    def recibir_mensaje(self):
        mensaje = self.s.recv(1024).decode()
        print(f'Otro: {mensaje}')
        if self.exit_request(mensaje): self.close()
    
    def close(self):
        print("Finalizando conexión...")
        self.s.close()
        sys.exit(0)

class Cliente(Messenger):
    def __init__(self, host, port):
        super().__init__(host, port)
    
    def start(self):
        self.s.connect((self.host, self.port))
        while True:
            self.enviar_mensaje()
            self.recibir_mensaje()

class Servidor(Messenger):
    def __init__(self, host, port):
        super().__init__(host, port)
    
    def bind(self):
        self.s.bind((self.host, self.port))
        self.s.listen(5)
    
    def start(self):
        self.bind()
        self.s, addr = self.s.accept()

        while True:
            self.enviar_mensaje()
            self.recibir_mensaje()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--client', action='store_true')
    parser.add_argument('-i', '--ip', default='127.0.0.1')
    parser.add_argument('-p', '--port', type=int, default=5000)
    args = parser.parse_args()

    messenger_class = Cliente if args.client else Servidor

    messenger = messenger_class(args.ip, args.port)
    messenger.start()