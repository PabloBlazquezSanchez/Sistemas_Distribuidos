HOST = localhost
PORT = 10001

all: compile

compile:
	protoc --python_out=. math.proto

clean:
	$(RM) *_pb2* *~
	$(RM) -rf __pycache__

exec_server:
	python3 server.py $(HOST):$(PORT)

# usage: python3 client.py <host:port> <operation> <num1> <num2> ...
# operation: add | multiply
exec_client:
	python3 client.py $(HOST):$(PORT) add 1 2 3 4 5
	python3 client.py $(HOST):$(PORT) multiply 1 2 3 4 5
# 	Operacion no permitida para probar el error
	python3 client.py $(HOST):$(PORT) subtract 1 2 3 4 5