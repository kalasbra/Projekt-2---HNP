# Import necessary libraries
import paho.mqtt.client as mqtt  # MQTT client library
import serial  # Serial communication library
import json  # JSON library for reading configuration data
import time  # Time library for timestamp
import struct  # Struct library for packing data

# Read configuration data from a JSON file
with open("hub/config.json") as config_file:
    config_data = json.load(config_file)

# Extract configuration data
name = config_data.get("name")  # Extract the "name" field from the JSON configuration
broker = config_data.get("broker")  # Extract the MQTT broker address
topic = config_data.get("topic")  # Extract the MQTT topic

# Create an MQTT client and register a callback for connect events
client = mqtt.Client()

# Connect to an MQTT broker with the provided configuration
client.connect(broker, port=1883, keepalive=60)

# Start a background loop that handles all MQTT broker communication
client.loop_start()

# Establish a serial connection with a device on COM3 at a baud rate of 115200
with serial.Serial("COM3", 115200, timeout=1) as ser:
    while True:
        # Get the current timestamp in seconds since the epoch
        ts = time.time()
        timeInt = int(ts)
        
        # Read a line from the serial device (terminated by '\n')
        line = ser.readline()

        # Check if a line was read (not empty)
        if len(line) != 0:
            # Convert the binary data to a string in UTF-8 encoding
            str = line.decode("utf-8")

            # Split the string into a list of values
            list_ = str.split()

            # Extract values from the list
            pico_id = list_[0]
            temp_id = list_[1]
            temp = float(list_[2])

            # Convert the temperature to a scaled integer value
            temp_trunk = int(temp * 1000)

            # Create the MQTT topic based on the configuration
            RealTopic = f"{topic}/{name}/{pico_id}/{temp_id}"

            # Pack the timestamp and temperature into a binary payload
            payload = struct.pack(">Ii", timeInt, temp_trunk)

            # Publish the data to the MQTT broker with Quality of Service (QoS) 1
            msg = client.publish(RealTopic, payload=payload, qos=1)

            # Wait for the message to be successfully published
            msg.wait_for_publish()
