#!/usr/bin/env python3

import argparse
import socket
import random
from PaulaCastillejoBravo_Protobuf_puerta_pb2 import Switchboard, Response

MSG_ID = 1  

class Controller:
    obstacleBase=( ['obstacle', 'clear'])
    OBSTACLE = random.choice(obstacleBase)
    motorBase=( ['damaged', 'functional'])
    MOTOR = random.choice(motorBase)
    
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port

    def send_message(self, msg):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.server_ip, self.server_port))

        client.send(msg.SerializeToString())

        response_data = client.recv(1024)
        response = Response()
        response.ParseFromString(response_data)

        client.close()
        return response

    def check_status(self):
        msg = Switchboard()
        msg.id = MSG_ID
        msg.option = Switchboard.STATE

        response = self.send_message(msg)
        return response.result

    def open_door(self, mode=Switchboard.VEHICLE, time=None):
        msg = Switchboard()
        msg.id = MSG_ID
        msg.option = Switchboard.OPEN
        msg.openTime = time
        msg.openDoor = Switchboard.VEHICLE
        if mode == 'person':
            msg.openDoor = Switchboard.PERSON
        msg.obstacle = Controller.OBSTACLE
        msg.motor = Controller.MOTOR

        response = self.send_message(msg)
        return response.result

    def close_door(self):
        msg = Switchboard()
        msg.id = MSG_ID
        msg.option = Switchboard.CLOSE
        msg.obstacle = Controller.OBSTACLE
        msg.motor = Controller.MOTOR

        response = self.send_message(msg)
        return response.result

def main():
    controller = Controller(args.server, 2002)

    if args.command == 'state':
        result = controller.check_status()

    if args.command == 'open':
        result = controller.open_door(args.mode, args.time)

    if args.command == 'close':
        result = controller.close_door()

    print(f'Result: {result} ')


parser = argparse.ArgumentParser(description='Door Controller')
parser.add_argument('-s', '--server', type=str, default='localhost', help='Server IP Address')

subparsers = parser.add_subparsers(dest='command', help='Commands', metavar='COMMAND')

# Open command with its subarguments
open_parser = subparsers.add_parser('open', help='Open door')
open_parser.add_argument('-t', '--time', type=int, default=0, help='Time to keep the door open in seconds')
open_parser.add_argument('-m', '--mode', choices=['vehicle', 'person'], default='vehicle', help='Mode to open the door')

close_parser = subparsers.add_parser('close', help='Close door')
get_parser = subparsers.add_parser('state', help='Check door status')
args = parser.parse_args()

if args.command is None:
    parser.print_help()
    exit(1)

main()