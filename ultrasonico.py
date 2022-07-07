#import RPi.GPIO as GPIO
#import Adafruit_DHT
#import time
#GPIO.setmode(GPIO.BCM)
from datetime import datetime
import json

class ultra:
    def __init__(self, sensor):
        self.sensor = sensor
        self.medicion=''
        self.dateTime=''

    def read(self, sensor):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(sensor.pines[0],GPIO.OUT)#trigger pin 21
        GPIO.setup(sensor.pines[1],GPIO.IN)#echo pin 20
        GPIO.output(sensor.pines[0], True)
        time.sleep(1)
        GPIO.output(sensor.pines[0], False)
        while GPIO.input(self.pines[1]) == False:
            start = time.time()
        while GPIO.input(self.pines [1]) == True:
            end = time.time()
        self.medicionU(sensor)
        sig_time = end-start
         #Centimetros:
        distance = sig_time / 0.000058
        dt = datetime.now()
        self.dicc(distance,dt)
        print('Distance: {} centimetros'.format(distance)+' at '+ dt)#fecha y hora en el json, junto con los datos y las lecturas, 
                                                            #regresada en cada lectura del sensor para despues insertarlo en el json
        GPIO.cleanup()#arreglo de objetos

    def dicc(self, d, dt):
        medicion={
            "id_sensor": self.sensor.id,
            "medicion": d,
            "date time": dt
        }
        with open('med.json', 'a') as file:
            json.dump(medicion,file,indent=6)

    def prueba(self):
        print(self.sensor)