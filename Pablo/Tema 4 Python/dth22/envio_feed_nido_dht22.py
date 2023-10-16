'''El código base para DHT22 está cogido de
https://tutorials-raspberrypi.com/raspberry-pi-measure-humidity-temperature-dht11-dht22/
En este programa se envían los datos de temperatura y humedad a la plataforma IoT Adafruit,
además de imprimirlos en pantalla'''

import time
import board
import adafruit_dht

#Primera cosa añadida al código ejemplo de la web anterior sobre el dht, ahora para enviar datos a adafruit
#La librería adafruit-io tiene que estar instalada
from Adafruit_IO import Client
aio = Client('nidoherrera', 'aio_CPfH96WOqmhkfCyrN0RivteUeYRC')
 
# Initial the dht device, with data pin connected to:
# dhtDevice = adafruit_dht.DHT22(board.D4)
 
# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
#dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

while True:
    try:
        # Print the values to the serial port
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} C    Humidity: {}% ".format(
                temperature, humidity
            )
        )
 
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

#Segunda cosa añadida al ejemplo de la web sobre el dht, ahora para enviar datos a adafruit
#tempinterior y huminterior no son los nombres de los feeds, son sus keys
#No se puede mandar más de 30 datos por minuto en nuestra cuenta de adafruit
    aio.send('tempinterior', temperature)
    aio.send('huminterior', humidity)

    time.sleep(4.0)