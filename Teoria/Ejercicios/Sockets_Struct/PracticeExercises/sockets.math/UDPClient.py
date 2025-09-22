import socket
import struct
import sys

"""
Usage: python3 UDPClient.py <server_host:port> {{add|mul}} <num1> <num2> [<num3> ... <numN>]
Example: python3 UDPClient.py localhost:12345 add 5 10 15
"""

def main():
    if len(sys.argv) < 5:
        print("Usage: python3 UDPClient.py <server_host:port> {{add|mul}} <num1> <num2> [<num3> ... <numN>]")
        return

    host, port = sys.argv[1].split(':')
    port = int(port)
    operation = sys.argv[2]
    numbers = [int(num) for num in sys.argv[3:]]

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        data_format = f'!3s{len(numbers)}h'

        print(f"Data format: {data_format}")

        serialized = struct.pack(data_format, operation.encode(), *numbers)

        print(f"Serialized data: {serialized}")

        print(f"Sending data to {host}:{port}")

        sock.sendto(serialized, (host, port))

        print(f"Waiting for response from {host}:{port}")
        data = sock.recv(1024)

        result = struct.unpack('!i', data)[0]
        print(f"Result from server: {result}")

if __name__ == "__main__":
    main()