import math

class circulo():
    #Consructor
    def __init__(self, radio):
        self.radio = radio
        
    #Metodos
    def calcular_area(self):
        return math.pi * math.pow(self.radio, 2)   
    
    def calcular_perimetro(self):
        return 2 * self.radio * math.pi
    
    def calcular_diametro(self):
        return 2*self.radio
    
c1 = circulo(5)

print(c1.calcular_area())
print(c1.calcular_perimetro())
print(c1.calcular_diametro())