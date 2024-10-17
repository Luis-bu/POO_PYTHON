class Computadora():
    #Constructor en Python
    def __init__ (self, procesador, tarjeta_grafica, ram):
        
        self.procesador = procesador
        self.tarjetagrafica =   tarjeta_grafica
        self.ram = ram   
    
    #Los métodos deben tener el párametro self
    def ejecutar(self):
        print(f"El {self.procesador} Esta ejecutando un programa")

#Instanciamos
pc1 = Computadora("i5", "GTX-3060", 8)      
pc2 = Computadora("i7", "4090", 16) 

pc1.ejecutar()