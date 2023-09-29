import paho.mqtt.client as mqtt
import serial
import json

with open("config.json") as config_file:
    config_data = json.load(config_file) 
  
name = config_data.get("name")
broker = config_data.get("broker")
topic = config_data.get("topic")

# Create a MQTT client and register a callback for connect events
client = mqtt.Client()
# Connect to a broker
client.connect(broker, port=1883, keepalive=60)
# Start a background loop that handles all broker communication
client.loop_start()

with serial.Serial("COM3", 9600, timeout=1) as ser:
    while True:
        line = ser.readline()   # read a '\n' terminated line
        if len(line) != 0:
            str = line.decode("utf-8")
            mystring = str.split()
            part1 = mystring[0]
            part2 = mystring[1]
            tippelitopic = topic/name/part1/part2
            
            msg = client.publish("tippelitopic", payload=f"Oscar: {line}", qos=1) 
            msg.wait_for_publish()

