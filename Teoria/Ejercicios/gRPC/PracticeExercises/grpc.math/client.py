import sys
import grpc
import math_pb2
import math_pb2_grpc

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 client.py <host:port> <operation> <num1> <num2> ...")
        return

    host, port = sys.argv[1].split(':')
    port = int(port)

    operation = sys.argv[2]
    numbers = list(map(int, sys.argv[3:]))

    with grpc.insecure_channel(f"{host}:{port}") as channel:
        stub = math_pb2_grpc.MathStub(channel)
        if operation == "add":
            response = stub.add(math_pb2.MathRequest(numbers=numbers))
        elif operation == "multiply":
            response = stub.multiply(math_pb2.MathRequest(numbers=numbers))
        else:
            print("Unknown operation:", operation)
            return

    print("Response:", response.result)

if __name__ == "__main__":
    main()