from sensores import Sensores
import json

class Interfaz():
    def __init__(self):
        self.listaSensores = Sensores()

    def load(self):
        with open('data.json','r') as file:
            data=json.load(file)
            i=int(0)
            for doc in data:
                sensor=Sensores(doc['id'],doc['pines'],doc['tipo'],doc['nombre'])
                self.listaSensores.add(sensor)
                

    def newS(self):
        s=Sensores()
        s.id=input("Identificador del sensor: ")
        pr=int(input("numero de pines del sensor: "))
        c=0
        while(c <= pr-1):
            pin=int(input("introduzca el numero del pin: "))
            s.pines.append(pin)
            c+=1
        s.tipo=input("Tipo de sensor: ")
        s.nombre=input("Nombre del sensor: ")
        self.listaSensores.add(s)
        self.listaSensores.obj()

    def modS(self):
        self.getSensores()
        print("")
        id=input("Ingrese el numero del grupo que desea modificar: ")
        s=Sensores()
        s.get[id]
        cadena = input("Ingrese el id del sensor: ")
        s.id=cadena
        qst = input("desea modificar el numero de los pines? Y/N ")
        if (qst== "Y"):
            for x in s.pines:
                cadena1 = input("Ingrese el numero del pin: ")
                s.pines.append(cadena1)
        cadena2 = input("Ingrese el tipo de sensor: ")
        s.tipo=cadena2
        cadena3 = input("Ingrese el nombre del sensor: ")
        s.nombre = cadena3
        self.listaSensores.obj()

    def getSensores(self, lista=None):
        print("-" * 10 + " Datos de los sensores " + "-" * 10)
        if (lista == None):
            myLista = self.listaSensores
        else:
            myLista = lista
        print(" # sensor "+" " * 5 +"ID"+ " " * 5 + " pines "+ " " * 5+" tipo "+" " * 5+" nombre ")
        i=0
        for x in myLista:
            print(str(i)+" " * 10 + str(x.id) + " " * 3 + str(x.pines) + " " * 5 + str(x.tipo) + " " * 5 + str(x.nombre))
            i+=1

    def delSen(self):
        self.getSensores()
        id=input("Ingrese el numero del grupo que desea modificar: ")
        s=self.listaSensores.get()[id]
        self.listaSensores.dlt(s)
        self.listaSensores.obj()

    def menu(self):
        s=Sensores()
        self.load()
        x=8
        while x!=0:
            print("-" * 7 + " Menu sensores " + "-" * 7)
            print("1.- Agregar sensor")
            print("2.- Modificar sensor")
            print("3.- Eliminar sensor")
            print("4.- Listar sensores")
            print("5.- Medir")
            print("0.- Salir")
            x=int(input("ingrese una opcion: "))
            if x==1:
                self.newS()
            elif x==2:
                self.modS()
            elif x==3:
                self.delSen()
            elif x==4:
                self.getSensores()
                print("-" * 10 + "Oprime enter para continuar" + "-" * 10)
                input()
            elif x== 5:
                self.getSensores()
                id=int(input("Ingrese el numero del grupo que desea modificar: "))
                sensor=self.listaSensores.get()[id]
                print(sensor)
                print(s.lecturas(sensor))
            elif x==0:
                print("saliendo...")
                break
            else:
                print("Opcion invalida, intente nuevamente (presione enter) ")
                input()

if (__name__=='__main__'):
    In=Interfaz()
    In.menu()


