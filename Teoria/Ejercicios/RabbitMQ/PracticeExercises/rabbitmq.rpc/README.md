# Indirect RPC

## English Statement

In this exercise, you have to simulate an RPC (Remote Procedure Call) with RabbitMQ. For this, you need to create two programs, one that acts as a client and another as a server. The server only carries out one task, which is to calculate the factorial of a number. The client, on the other hand, sends a number to the server and waits for it to return the result of the factorial calculation.

To implement this application, you will have to create two message queues, one for handling requests and another for handling responses. The client will send a message to the request queue and wait for the server to send a message to the response queue. The server, in turn, will be listening on the request queue and will send the result to the response queue.

Keep in mind that the client can specify, when posting a message, which is the response message queue to which the server should send the result. In addition, it will be necessary to link each request with its corresponding response. To do this, you can use the message correlation identifier provided by RabbitMQ:

```python
properties = pika.BasicProperties(
    reply_to = results_queue,
    correlation_id = correlation_id
)
```

Install RabbitMQ if not already installed:

```bash
sudo apt install rabbitmq-server
```

Then start the RabbitMQ broker:

```bash
sudo service rabbitmq-server start
```

## Spanish Statement

En este ejercicio, tienes que simular una RPC (Llamada a Procedimiento Remoto) con RabbitMQ. Para ello, necesitas crear dos programas, uno que actúe como cliente y otro como servidor. El servidor sólo realiza una tarea, que es calcular el factorial de un número. El cliente, por su parte, envía un número al servidor y espera a que éste le devuelva el resultado del cálculo del factorial.

Para implementar esta aplicación, tendrás que crear dos colas de mensajes, una para gestionar las peticiones y otra para gestionar las respuestas. El cliente enviará un mensaje a la cola de peticiones y esperará a que el servidor envíe un mensaje a la cola de respuestas. El servidor, a su vez, estará escuchando en la cola de peticiones y enviará el resultado a la cola de respuestas.

Ten en cuenta que el cliente puede especificar, al publicar un mensaje, cuál es la cola de mensajes de respuesta a la que el servidor debe enviar el resultado. Además, será necesario vincular cada petición con su correspondiente respuesta. Para ello, puedes utilizar el identificador de correlación de mensajes que proporciona RabbitMQ:

```python
properties = pika.BasicProperties(
    reply_to = results_queue,
    correlation_id = correlation_id
)
```

Instala RabbitMQ si no está instalado todavía:

```bash
sudo apt install rabbitmq-server
```

Luego inicia el broker de RabbitMQ:

```bash
sudo service rabbitmq-server start
```
