PYTHON=python3
VENV=venv
ACTIVATE=. $(VENV)/bin/activate;
HOST = localhost
PORT = 10001

.PHONY: all install proto run-server run-client clean distclean

all: install proto

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(ACTIVATE) pip install --upgrade pip
	$(ACTIVATE) pip install -r requirements.txt

proto:
	$(ACTIVATE) python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. math.proto

run-server:
	$(ACTIVATE) python server.py $(HOST):$(PORT)

run-client:
	$(ACTIVATE) python client.py $(HOST):$(PORT) add 1 2 3 4 5
	$(ACTIVATE) python client.py $(HOST):$(PORT) multiply 1 2 3 4 5

#	Operación no permitida para probar el error
	$(ACTIVATE) python client.py $(HOST):$(PORT) subtract 1 2 3 4 5

clean:
	rm -f math_pb2.py math_pb2_grpc.py
	rm -rf __pycache__

distclean: clean
	rm -rf $(VENV)
