#!/usr/bin/python
import random
import time

from paho.mqtt import client as mqtt_client

broker = '192.168.6.67'
port = 1883
topic = 'smoker/temp'
client_id = 'pismoker'

# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # x_client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def send_message(client, message):
    result = client.publish(topic, message)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print("Send `%s` to topic `%s`", message, topic)
    else:
        print("Failed to send message to topic %s", topic)


