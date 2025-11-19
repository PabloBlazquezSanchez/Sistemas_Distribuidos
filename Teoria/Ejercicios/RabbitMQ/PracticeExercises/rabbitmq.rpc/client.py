#!/usr/bin/python3
import pika
import uuid
import sys


class FibonacciRpcClient(object):
    def __init__(self):
        print("[DEBUG] Iniciando cliente RPC...")
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )
        print("[DEBUG] Conexión establecida con RabbitMQ")

        self.channel = self.connection.channel()
        print("[DEBUG] Canal creado")

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue
        print(f"[DEBUG] Cola de callback creada: {self.callback_queue}")

        self.channel.basic_consume(
            on_message_callback=self.on_response,
            auto_ack=True,
            queue=self.callback_queue
        )
        print("[DEBUG] Consumidor configurado en la cola de callback")

    def on_response(self, ch, method, props, body):
        print(f"[DEBUG] Respuesta recibida - Correlation ID: {props.correlation_id}")
        print(f"[DEBUG] Correlation ID esperado: {self.corr_id}")
        if self.corr_id == props.correlation_id:
            self.response = body
            print(f"[DEBUG] Respuesta válida recibida: {body}")
        else:
            print("[DEBUG] Correlation ID no coincide, ignorando mensaje")

    def call(self, n):
        print(f"[DEBUG] Llamando a fibonacci({n})")
        self.response = None
        self.corr_id = str(uuid.uuid4())
        print(f"[DEBUG] Correlation ID generado: {self.corr_id}")
        
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            body=str(n),
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            )
        )
        print(f"[DEBUG] Mensaje publicado en 'rpc_queue' con n={n}")

        print("[DEBUG] Esperando respuesta...")
        while self.response is None:
            self.connection.process_data_events()

        print(f"[DEBUG] Respuesta procesada: {self.response}")
        return int(self.response)


print("[DEBUG] Creando instancia de FibonacciRpcClient")
fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(%d)" % int(sys.argv[1]))
response = fibonacci_rpc.call(int(sys.argv[1]))
print(" [.] Got %r" % response)
print("[DEBUG] Proceso completado")