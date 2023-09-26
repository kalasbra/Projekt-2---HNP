# import time
# import machine
# import onewire, ds18x20

# # the device is on GPIO12
# dat = machine.Pin(16)

# # create the onewire object
# ds = ds18x20.DS18X20(onewire.OneWire(dat))

# # scan for devices on the bus
# roms = ds.scan()
# print('found devices:', roms)

# # loop 10 times and print all temperatures
# for i in range(10):
#     print('temperatures:', end=' ')
#     ds.convert_temp()
#     time.sleep_ms(750)
#     for rom in roms:
#         print(ds.read_temp(rom), end=' ')
#     print()

import machine, onewire, ds18x20, time
 
ds_pin = machine.Pin(16)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
 
roms = ds_sensor.scan()
print('Found DS18B20:', roms)

if not roms:
    raise RuntimeError("Found no DS18B20")

while True: 
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
   print('temp:', end=' ')
   print(ds_sensor.read_temp(rom))
  time.sleep(1)
