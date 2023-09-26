import json


with open('sensor/config.json', 'r') as config_file:
  config_data = json.load(config_file)
  
pin = config_data.get("pin")
interval = config_data.get("interval")

print(pin)
print(interval)