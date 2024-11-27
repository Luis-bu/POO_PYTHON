#ISP (Principio de segregación de la Interfaz)

#No podemos agregar una interfaz que el cliente no quiera usar

from abc import ABC, abstractmethod

#En lugar de asignar metodos en un clase que algunos objetos no necesitan usar(ej: una persona puede comer, dormir y trabajar. Pero un robot solo puede trabajar, usamos multiple herencia)

class Trabajador(ABC):
    
    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):
    
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador, Comedor, Durmiente):
    
    def trabajar(self):
        print("El humano esta trabajando")
    
    def comer(self):
        print("El humano esta comiendo")
    
    def dormir(self):
        print("El humano esta durmiendo")
        
#Como dijimos, el robot solo puede trabajar
class Robot(Trabajador):
    
    def trabajar(self):
        print("El robot esta trabajando")        