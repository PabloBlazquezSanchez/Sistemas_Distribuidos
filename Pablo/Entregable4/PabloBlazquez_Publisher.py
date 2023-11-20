import json
from time import sleep
import sys
import paho.mqtt.client as mqtt

#ssdd/ejercicio4/persons/codes
#ssdd/ejercicio4/persons/results

def build_event(codigo):
    return{
        'code': codigo,
        'fullname': 'Pablo Blázquez',
        'dni': '02338460'  # 8 characters
    }

def callback(client, userdata, message):
    decoded = json.loads(message.payload.decode())
    print("topic: {}, msg: {}".format(
        message.topic, decoded))

    print(decoded)
    publisher.publish('ssdd/ejercicio4/persons/result', json.dumps(build_event(decoded)))

if len(sys.argv) < 3:
    print("Uso: ./PabloBlazquez_Publisher.py <IP> <host>")
    exit()

publisher = mqtt.Client()
publisher.on_message= callback
publisher.connect(sys.argv[1])
publisher.subscribe('ssdd/ejercicio4/persons/codes')