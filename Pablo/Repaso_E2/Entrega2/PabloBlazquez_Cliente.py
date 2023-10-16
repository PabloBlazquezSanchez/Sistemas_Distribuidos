import sys
import socket
import person_pb2

if len(sys.argv) < 2:
    print("Uso: ./PabloBlazquez_Cliente.py <host>")
    exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destino = (sys.argv[1], 4080)

lector = person_pb2.Person()

lector.name = "Pablo Blázquez Sánchez"
lector.dni = 2338460
lector.email.extend(["pablo.blazquez", "alu", "uclm", "es"])

dato = lector.SerializeToString()
sock.sendto(dato, destino)

dato_respuesta = sock.recv(1024)
respuesta = person_pb2.Result()
respuesta.ParseFromString(dato_respuesta)
print(respuesta)

sock.close()