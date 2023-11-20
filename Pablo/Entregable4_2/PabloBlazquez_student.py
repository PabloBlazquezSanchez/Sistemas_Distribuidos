#!/usr/bin/python3

import pika
import uuid

#'192.168.8.224'

class App:
    def __init__(self, broker_host):
        self.broker_host = "localhost"

        #credentials = pika.PlainCredentials('ssdd', 'student')
        self.parameters = pika.ConnectionParameters(
            host=broker_host,
            #credentials=credentials
        )

        self.get_code()

    def get_code(self):
        self.code_connection = pika.BlockingConnection(self.parameters)
        self.channel = self.code_connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            on_message_callback=self.callback,
            auto_ack=False,
            queue=self.callback_queue
        )
        print("Bien")
        self.callback

    def callback(self, ch, method, props, body):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        message = body.decode("UTF-8")
        print(message)
        self.channel.basic_publish(
            exchange='results',
            routing_key='codes',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            )
        )
        self.code_connection.close()


student = App("localhost")
