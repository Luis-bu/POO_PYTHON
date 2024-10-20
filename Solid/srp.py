#SRP (Principio de responsabilidad única)
#Cada cosa (ej: una clase) debe cumplir con una única función

class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
    
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("El auto se ha movido de forma exitosa")
        else:
            print("No hay suficiente combustible")
    
    def get_posicion(self):
        return self.posicion
    
class Tanque_de_combustible():
    def __init__(self):
        self.combustible = 100
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
        
    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad 
    
tanque = Tanque_de_combustible()

carro = Auto(tanque)

print(carro.get_posicion())
print(carro.tanque.obtener_combustible())
carro.mover(200)
print(carro.get_posicion())
print(carro.tanque.obtener_combustible())