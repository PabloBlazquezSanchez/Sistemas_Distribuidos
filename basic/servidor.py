import socket
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(('127.0.0.1', 1234))
        msg, addr = s.recvfrom(1024)
        s.close()
    try:
        print(msg.decode("ascii"))
    except UnicodeDecodeError:
        print("Error al intentar decodificar el mensaje")