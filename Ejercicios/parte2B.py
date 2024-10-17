class Animal():
    def comer(self):
        print("Comiendo")

class Mamífero(Animal):
    def amamantar(self):
        print("Amamantando")
    
class Ave(Animal): 
    def volar(self):
        print("Volando")

class Murcielago(Mamífero, Ave):
    def __init__(self):
        super().__init__()
       
m1 = Murcielago()
m1.amamantar()
m1.volar()        
m1.comer()

print(Murcielago.mro())