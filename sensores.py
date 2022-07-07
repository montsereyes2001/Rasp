#import RPi.GPIO as GPIO
#import Adafruit_DHT
#import time
#GPIO.setmode(GPIO.BCM)
import json
from datetime import datetime
#from pymongo import MongoClient
import ultrasonico 

class Sensores():
    def __init__(self, id='', pines=[],tipo='', nombre=''):
        self.id=id
        self.pines=pines
        self.tipo=tipo
        self.nombre=nombre
        self.__idx__=0
        self.listaSensores = list()
    
    def add(self,sensor):
        self.listaSensores.append(sensor)

    def upd(self, index,sensor):
        self.listaSensores[index] = sensor

    def dlt(self,sensor):
        self.listaSensores.remove(sensor)
    
    def get(self):
        return self.listaSensores

    def __str__(self):
        return str(self.id)+" "+str(self.pines)+" "+str(self.tipo)+" "+str(self.nombre)+" "+str(self.listaSensores)

    def dicc(self):
        x = {
            "id":self.id,
            "pines": self.pines,
            "tipo": self.tipo,
            "nombre": self.nombre
        }
        return x

    def obj(self):
        lista=list()
        for x in self.listaSensores:
            lista.append(x.dicc())
        with open('data.json','w') as file:
            json.dump(lista,file,indent=6)
        return lista

    """def save(self):
            myclient = MongoClient("mongodb://localhost:27017/")
            db = myclient["d"] 
            Collection = db["Sensores"]   
            with open('med.json') as file: 
                file_data = json.load(file) 
            if isinstance(file_data, list): 
                Collection.insert_many(file_data)   
            else: 
                Collection.insert_one(file_data)"""

    def __iter__(self):
            self.__idx__ = 0
            return self

    def __next__(self):
        if self.__idx__ < len(self.listaSensores):
            x = self.listaSensores[self.__idx__]
            self.__idx__ += 1
            return x
        else:
            raise StopIteration

    def lecturas(self,sensor):
        if(sensor.tipo == 'US'):
            #self.ultra(sensor)
            print("----")
            u=ultrasonico.ultra()
            u.read()
            u.prueba()
            print("----")
        elif (sensor.tipo == 'TH'):
            self.temHum(sensor)
        #elif (sensor.id == 'numPad'):
         #   self.numPad(sensor)
        else:
            return 'el sensor no es valido'
    
    def ultra(self,sensor):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(sensor.pines[0],GPIO.OUT)
        GPIO.setup(sensor.pines[1],GPIO.IN)
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
        medicion={
            "id_sensor": sensor.id,
            "medicion": distance,
            "date time": dt
        }
        with open('med.json', 'a') as file:
            json.dump(medicion,file,indent=6)
        #self.save()
        print('Distance: {} centimetros'.format(distance)+' at '+ dt)#fecha y hora en el json, junto con los datos y las lecturas, 
                                                            #regresada en cada lectura del sensor para despues insertarlo en el json
        
        GPIO.cleanup()#arreglo de objetos

    #def medJson(self):

    #def ultra1(self,sensor):
     #   return sensor
    #def temHum1(self,sensor):
     #   return sensor

    def temHum(self,sensor):
        print('Inicia')
        sensor = Adafruit_DHT.DHT11 #Cambia por DHT22 y si usas dicho sensor
        #pin = sensor.pines[0] #Pin en la raspberry donde conectamos el sensor
        for pin in sensor.pines:
            p=pin
        print('Leyendo')
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, p)
        print ('Humedad: ' , humedad + ' at '+dt)
        print ('Temperatura: ' , temperatura + ' at '+dt)
        dt = datetime.now()
        time.sleep(0.25) #Cada segundo se evalúa el sensor
        
        #debe regresar dos objetos, uno de temperatura y uno de humedad, donde todos regresan arreglos.
    #def numPad(self, sensor):
     #   i=0
      #  for x in sensor.pines:
       #     i+=1