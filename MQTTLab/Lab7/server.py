import sys
import paho.mqtt.client as mqtt

topic = "id/yourname/sensor/evt/humidity"
server = "iotlab101.io7lab.com"

def on_connect(client, userdata, flags, rc):
    print("Connected with RC : " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    humidity = float(msg.payload.decode('utf-8'))
    if humidity > 50:
        client.publish("id/yourname/relay/cmd", "on")
    else:
        client.publish("id/yourname/relay/cmd", "off")

client = mqtt.Client()
client.connect(server, 1883, 60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
