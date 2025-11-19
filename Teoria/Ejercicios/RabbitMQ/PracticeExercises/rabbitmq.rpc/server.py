#!/usr/bin/python3
import pika


print("[DEBUG] Iniciando servidor RPC...")
localhost = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(localhost)
print("[DEBUG] Conexión establecida con RabbitMQ")

channel = connection.channel()
print("[DEBUG] Canal creado")

print("[DEBUG] Eliminando cola 'rpc_queue' si existe...")
channel.queue_delete(queue='rpc_queue')
print("[DEBUG] Cola eliminada")

channel.queue_declare(queue='rpc_queue')
print("[DEBUG] Cola 'rpc_queue' declarada")


def fib(n):
    print(f"[DEBUG] Calculando fibonacci({n})")
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    print(f"[DEBUG] fibonacci({n}) = {result}")
    return result


def on_request(ch, method, props, body):
    print(f"[DEBUG] Solicitud recibida")
    print(f"[DEBUG] Body: {body}")
    print(f"[DEBUG] Correlation ID: {props.correlation_id}")
    print(f"[DEBUG] Reply to: {props.reply_to}")
    
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n)
    print(f"[DEBUG] Resultado calculado: {response}")

    print(f"[DEBUG] Enviando respuesta a '{props.reply_to}'")
    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        body=str(response),
        properties=pika.BasicProperties(
            correlation_id=props.correlation_id
        ),
    )
    print("[DEBUG] Respuesta enviada")

    print(f"[DEBUG] Enviando ACK con delivery_tag: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("[DEBUG] ACK enviado")


print("[DEBUG] Configurando QoS con prefetch_count=1")
channel.basic_qos(prefetch_count=1)

print("[DEBUG] Configurando consumidor en 'rpc_queue'")
channel.basic_consume(on_message_callback=on_request, queue='rpc_queue')

print("[*] Waiting for messages. press Ctrl+C to exit")

try:
    print("[DEBUG] Iniciando consumo de mensajes...")
    channel.start_consuming()
except KeyboardInterrupt:
    print("\n[DEBUG] Interrupción detectada (Ctrl+C)")
    print("\nStopping server...")
    connection.close()
    print("[DEBUG] Conexión cerrada")