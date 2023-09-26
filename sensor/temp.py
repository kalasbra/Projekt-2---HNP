import time
import machine
import onewire
import ds18x20
import json
import binascii

pico_id = machine.unique_id()
pico_id_hex = binascii.hexlify(machine.unique_id()).upper()

with open('sensor/config.json', 'r') as config_file:
  config_data = json.load(config_file)
  
pin = config_data.get("pin")
interval = config_data.get("interval")

ds_pin = machine.Pin(pin)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
 
roms = ds_sensor.scan() 
print('Found DS18B20:', roms)

if not roms:
    raise RuntimeError("Found no DS18B20")

while True: 
  ds_sensor.convert_temp()
  time.sleep_ms(interval)
  for rom in roms:
   print('temp:', end=' ')
   print(ds_sensor.read_temp(rom))
  time.sleep(1)
