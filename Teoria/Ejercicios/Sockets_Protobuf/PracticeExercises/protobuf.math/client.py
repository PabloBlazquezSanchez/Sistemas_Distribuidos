import socket
from math_pb2 import MathRequest, MathResponse
import sys

# usage: python3 client.py <host:port> <operation> <num1> <num2> ...
# operation: add | multiply

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 client.py <host:port> <operation> <num1> <num2> ...")
        return

    host, port = sys.argv[1].split(':')
    port = int(port)
    operation = sys.argv[2].lower()
    numbers = list(map(int, sys.argv[3:]))

    request = MathRequest()
    if operation == 'add':
        request.operation = MathRequest.OperationType.ADD
    elif operation == 'multiply':
        request.operation = MathRequest.OperationType.MULTIPLY
    else:
        print("Invalid operation. Use 'add' or 'multiply'.")
        return

    request.numbers.extend(numbers)

    sock = socket.socket(type=socket.SOCK_DGRAM)
    sock.sendto(request.SerializeToString(), (host, port))

    print("Request sent, waiting for response...")
    data, _ = sock.recvfrom(1024)
    print(f"Response received: {data}")
    response = MathResponse()
    response.ParseFromString(data)

    print(f"Result: {response.result}")

if __name__ == "__main__":
    main()