class auto():
    def __init__(self):
        self.estado = "Apagado"
    
    def encender(self):
        self.estado = "Encendido"
        print("El auto se ha encendido correctamente")
    
    def conducir(self):
        if self.estado == "Apagado":
            self.encender()
            print("Conduciendo el auto")

carro = auto()
carro.conducir()