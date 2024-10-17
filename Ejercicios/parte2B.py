class Animal():
    def __init__(self):
        pass
    
    def comer():
        print("Comiendo")

class Mamífero():
    def __init__(self):
        pass
    
    def amamantar(self):
        print("Amamantando")
    
class Ave():
    def __init__(self):
        pass
    
    def volar(self):
        print("Volando")

class Murcielago(Mamífero, Ave):
    def __init__(self):
        super().__init__()
       
m1 = Murcielago()
m1.amamantar()
m1.volar()        
      