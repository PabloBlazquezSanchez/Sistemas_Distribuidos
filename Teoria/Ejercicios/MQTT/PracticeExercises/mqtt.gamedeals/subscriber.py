#!/usr/bin/python3

import paho.mqtt.client as mqtt
import json
import argparse

def print_hot_deal(deal):
    print(f'[!] HOT DEAL\n'
        + f'\t{deal["name"]} by {deal["developer"]} ({deal["type"]})\n'
        + f'\tOn sale with a {deal["discount"]}% discount\n\n')

def print_deal(deal):
    print(f'[ ] New deal\n'
        + f'\t{deal["name"]} by {deal["developer"]} ({deal["type"]})\n'
        + f'\tOn sale with a {deal["discount"]}% discount\n\n')

def on_message(client, userdata, msg):
    topics = msg.topic.split('/')

    deal = json.loads(msg.payload)
    deal['developer'] = topics[3]
    deal['type'] = topics[2]

    print_deal(deal) if deal['discount'] < 50 else print_hot_deal(deal)

parser = argparse.ArgumentParser(description="MQTT Subscriber for Game Deals")

parser.add_argument(
    '-d', '--developer',
    nargs='+',
    default=['+'],
    help="Filter by game developer(s). Use '+' for no filter.",
    required=False)

parser.add_argument(
    '-t', '--type',
    nargs='+',
    default=['+'],
    help="Filter by game type(s). Use '+' for no filter.",
    required=False)

args = parser.parse_args()

subscriber = mqtt.Client()
subscriber.on_message = on_message
subscriber.connect('localhost')

for vg_type in args.type:
    for vg_developer in args.developer:
        topic = f'videogames/deals/{vg_type.lower()}/{vg_developer.lower()}'
        subscriber.subscribe(topic)
        print(f"Subscribed to: {topic}")

try:
    subscriber.loop_forever()
except KeyboardInterrupt:
    print("Subscriber disconnected.")