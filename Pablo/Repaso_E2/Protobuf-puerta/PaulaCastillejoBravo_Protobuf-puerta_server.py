#!/usr/bin/env python3

import socket
from PaulaCastillejoBravo_Protobuf_puerta_pb2 import Switchboard, Response

class Door:
    CLOSED = Response.DOOR_JUST_CLOSE
    OPEN = Response.DOOR_JUST_OPEN

    def __init__(self):
        self.status = Door.CLOSED

    def open(self, mode, time, obstacle, motor):
        if self.status == Door.OPEN:
            print(f'[!] Door already open.')
            return Response.DOOR_JUST_OPEN
        
        if obstacle == 'obstacle':
            print(f'[!] Obstacle encountered.')
            return Response.OBSTACLE
        
        if motor == 'damaged':
            print(f'[!] Motor not response.')
            return Response.NO_MOTOR

        # Implement something for random errors and time
        self.status = Door.OPEN
        print(f'[-] Door opened. Mode: {mode}. Time: {time}')
        return Response.OK

    def close(self, obstacle, motor):
        if self.status == Door.CLOSED:
            print(f'[!] Door already closed.')
            return Response.DOOR_JUST_CLOSE
        
        if obstacle == 'obstacle':
            print(f'[!] Obstacle encountered.')
            return Response.OBSTACLE
        
        if motor == 'damaged':
            print(f'[!] Motor not response.')
            return Response.NO_MOTOR

        # Implement something for random errors
        self.status = Door.CLOSED
        print('[-] Door closed.')
        return Response.OK
    
    def state(self):
        if self.status == Door.CLOSED:
            print(f'[?] Door closed.')
            return Response.OK
        elif self.status == Door.OPEN:
            print(f'[?] Door opened')
            return Response.OK

def handle_client(client, door):
    request_data = client.recv(1024)
    switchboard = Switchboard()
    switchboard.ParseFromString(request_data)

    response = Response()
    response.id = switchboard.id

    if switchboard.option == Switchboard.STATE:
        response.result = door.state()

    if switchboard.option == Switchboard.OPEN:
        response.result = door.open(switchboard.openDoor, switchboard.openTime, switchboard.obstacle, switchboard.motor)

    if switchboard.option == Switchboard.CLOSE:
        response.result = door.close(switchboard.obstacle, switchboard.motor)

    client.send(response.SerializeToString())
    client.close()

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 2002))
    server.listen(5)
    print('Servidor escuchando en el puerto 2002')
    
    door = Door()
    
    while True:
        client, address = server.accept()
        handle_client(client, door)