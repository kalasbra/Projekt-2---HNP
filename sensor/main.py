import time
import machine
import onewire
import ds18x20
import ujson

# Load configuration data from the "config.json" file
with open("config.json") as config_file:
    config_data = ujson.load(config_file)

# Function to get the unique ID of the Pico in hexadecimal format
def pico_id():
    pico_id = machine.unique_id()
    pico_id_hex = pico_id.hex()
    return pico_id_hex

# Function to convert a temperature sensor ID to hexadecimal format
def temp_id(temp_id):
    temp_id_hex = temp_id.hex()
    return temp_id_hex

# Retrieve configuration values from the loaded data
pin = config_data.get("pin")      # The pin for connecting the temperature sensor
interval = config_data.get("interval")  # Time interval for temperature readings

# Set up the temperature sensor on the specified pin
ds_pin = machine.Pin(pin)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

# Scan for DS18B20 temperature sensors and print their IDs
roms = ds_sensor.scan()
print('Found DS18B20:', roms)

# If no DS18B20 sensors are found, raise a runtime error
if not roms:
    raise RuntimeError("Found no DS18B20")

# Continuously read temperature data from the sensors
while True:
    ds_sensor.convert_temp()  # Start temperature conversion
    time.sleep_ms(750)  # Wait for the conversion to complete (750 milliseconds)

    # Iterate through the found sensor IDs and print temperature readings
    for id in roms:
        print(f"{pico_id()} {temp_id(id)} {ds_sensor.read_temp(id)}")

    time.sleep(interval)  # Wait for the specified interval before the next reading
