import grpc
import sys
import math
import factorial_checker_pb2
import factorial_checker_pb2_grpc
"""
* IP = 192.168.8.224
* Port = 4080
"""
DEF_PORT = 4080

if len(sys.argv) < 2:
    print("Uso: ./PabloBlazquez_Cliente.py <host>")
    exit()

channel = grpc.insecure_channel(f'{sys.argv[1]}:{DEF_PORT}')
stub = factorial_checker_pb2_grpc.FactorialCheckerStub(channel)

lector_numero = factorial_checker_pb2.NumberRequest(email="Pablo.Blazquez@alu.uclm.es")

respuesta1 = stub.RequestRandomNumber(lector_numero)

print(respuesta1.number)

numfactorial = math.factorial(respuesta1.number)

print(numfactorial)

lector_checkRequest = factorial_checker_pb2.CheckRequest(email="Pablo.Blazquez@alu.uclm.es", factorial=numfactorial)

respuesta2 = stub.CheckFactorial(lector_checkRequest)

print(respuesta2.result)