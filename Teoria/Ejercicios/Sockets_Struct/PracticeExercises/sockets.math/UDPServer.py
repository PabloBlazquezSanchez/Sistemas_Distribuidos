import socket
import struct

host = ''
port = 12345

def mul(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

def sum(numbers):
    result = 0
    for n in numbers:
        result += n
    return result

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((host,port))
    while True:
        print("Waiting for data...")


        data, addr = sock.recvfrom(1024)

        print(f"Received data from {addr}: {data}")

        operation = struct.unpack('!3s', data[:3])[0].decode()

        if operation not in ['add', 'mul']:
            print(f"Invalid operation: {operation}")
            continue

        nums_format = f'!{(len(data)-3)//2}h'
        numbers = struct.unpack(nums_format, data[3:])

        print(f"Operation: {operation}, Numbers: {numbers}")

        result = sum(numbers) if operation == 'add' else mul(numbers)

        print(f"Sending result back to {addr}: {result}")
        sock.sendto(struct.pack('!i', result), addr)

        print(f"{addr} :: {operation} result = {result}")