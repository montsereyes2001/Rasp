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

    def read(self):
        GPIO.setmode(GPIO.BCM)
        T=self.sensor.pines[0]
        E=self.sensor.pines[1]
        GPIO.setup(T,GPIO.OUT)#trigger pin 21
        GPIO.setup(E,GPIO.IN)#echo pin 20
        GPIO.output(T, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(T, GPIO.LOW)
        while True:
            start = time.time()
            if GPIO.input(E) == GPIO.HIGH:
                break
        while True:
            end = time.time()
            if GPIO.input(E)==GPIO.LOW:
                break
        sig_time = end-start
         #Centimetros:
        distance = 34400*sig_time/2
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