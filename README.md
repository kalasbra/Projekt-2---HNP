projekt2

Detta är ett individuellt projekt där man skall bygga programvara för att dels läsa av en temperatursensor med
MicroPython på en Raspberry Pi Pico, dels skicka informationen vidare via UART till en Raspberry Pi Zero som i
sin tur skickar informationen vidare med Python och MQTT.

sensor/config.json:
Inställningar till GPIO pin och intervallen den skriver ut och läser av temp.

hub/config.json:
Inställningar till name, broker och topic till sändning av mqtt.

BOM:
Temperature probe DS18B20 - temp sensor
Usb till Micro-Usb kabel - koppla mellan datorn Och Raspberry Pico
Raspberry Pi Pico H
Kopplingskablar
Breadboard

Step-by-step:
1. Koppla upp sensorn till 3.3V, GND och GPIO16.
2. koppla upp Pico till datorn.
3. kopiera över main.py och config.json i sensor-katalogen till Pico:n via terminal med
4. "mpremote cp main.py" och "mpremote cp config.json" .
5. tryck Enter två gånger och skriv in "import main.py"

 - använd temp.py för debugging av raspberryn

MQTT:
1. skriv in COM-porten din Raspberry är kopplad till på rad 27 i hub/main.py. ex: COM3 ifall den är kopplad till COM3
2. kör sensor koden paralellt med hub-koden.  
4. använd hjälpfilen hw2_project_help-main från Classroom för att se om man får ut något.