import paho.mqtt.client as mqtt
import serial
import json
import time
import struct

with open("hub/config.json") as config_file:
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

with serial.Serial("COM3", 115200, timeout=1) as ser:
    while True:
        line = ser.readline()   # read a '\n' terminated line
        ts = time.time()
        timeInt = int(ts)
        if len(line) != 0:
            str = line.decode("utf-8")
            list_ = str.split()
            pico_id = list_[0]
            temp_id = list_[1]
            temp = float(list_[2])
            timeInt = int(ts)
            
            TempTrunk = int(temp*1000)
            RealTopic = f"{topic}/{name}/{pico_id}/{temp_id}"
            
            payload = struct.pack(">Ii", timeInt, TempTrunk)
            
            msg = client.publish(RealTopic, payload=payload, qos=1) 
            msg.wait_for_publish()

