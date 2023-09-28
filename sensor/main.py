import time
import machine
import onewire
import ds18x20
import ujson

with open("config.json") as config_file:
    config_data = ujson.load(config_file)         

def pico_id_get():
  pico_id = machine.unique_id()
  pico_id_hex = pico_id.hex()
  return pico_id_hex
  
def temp_id_get():
  temp_id = roms[0]
  temp_id_hex = temp_id.hex()
  return temp_id_hex

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
   print (f"{pico_id_get()} {temp_id_get()} {ds_sensor.read_temp(rom)}")
  time.sleep(1)
