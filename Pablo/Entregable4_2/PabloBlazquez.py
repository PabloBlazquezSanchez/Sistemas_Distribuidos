#!/usr/bin/python3

import pika
import uuid
import sys

# 192.168.8.224
# 5672

class RabbitMqt(object):
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    credentials = pika.PlainCredentials('ssdd', 'student')

    parameters = pika.ConnectionParameters(host="192.168.8.224", credentials=credentials)

    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    result = channel.queue_declare(queue='', exclusive=True)
    callback_queue = result.method.queue

    channel.basic_consume(
        on_message_callback=on_response,
        auto_ack=False,
        queue=callback_queue
    )
