import socket
import sys
from math_pb2 import MathRequest, MathResponse

def add(numbers):
    return sum(numbers)

def mul(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

sock = socket.socket(type=socket.SOCK_DGRAM)
# python3 server.py <host:port>
if len(sys.argv) == 2:
    host, port = sys.argv[1].split(':')
    port = int(port)
    sock.bind((host, port))
else:
    sock.bind(('', 10001))

while True:
    print("Waiting for request...")
    data, addr = sock.recvfrom(1024)
    print(f"Received request from {addr}")
    print(f"Request data: {data}")
    request = MathRequest()
    request.ParseFromString(data)

    response = MathResponse()
    if request.operation == MathRequest.OperationType.ADD:
        response.result = add(request.numbers)
    elif request.operation == MathRequest.OperationType.MULTIPLY:
        response.result = mul(request.numbers)

    sock.sendto(response.SerializeToString(), addr)
    print(f"Processed request from {addr}")