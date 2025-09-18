import socket
import sys
import struct

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ('localhost', 12345)



if __name__ == "__main__":
    server = sys.argv[1]
    num1 = sys.argv[2]
    num2 = sys.argv[3]

    print(f"Sending numbers {num1} and {num2} to server {server}")

    try:
        print("Creating packed message")
        message = struct.pack('!ii', int(num1), int(num2))
        print("Sending message")
        sock.sendto(message, (server.split(':')[0], int(server.split(':')[1])))
        print("Waiting for response")
        data, _ = sock.recvfrom(4096)
        print(data)
        print("Received:", struct.unpack('!i', data)[0])
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)