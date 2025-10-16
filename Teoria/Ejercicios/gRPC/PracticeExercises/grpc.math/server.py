from concurrent import futures
import sys
import grpc
import math_pb2
import math_pb2_grpc

class MathServicer(math_pb2_grpc.MathServicer):
    def add(self, request, context):
        result = sum(request.numbers)
        return math_pb2.MathResponse(result=result)

    def multiply(self, request, context):
        result = 1
        for num in request.numbers:
            result *= num
        return math_pb2.MathResponse(result=result)

def serve():
    if len(sys.argv) == 2:
        host, port = sys.argv[1].split(':')
        port = int(port)
    else:
        port = 10001
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    math_pb2_grpc.add_MathServicer_to_server(MathServicer(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    try:
        serve()
    except KeyboardInterrupt:
        print("Server stopped by user")