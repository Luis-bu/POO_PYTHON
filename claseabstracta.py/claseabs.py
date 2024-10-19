from abc import ABC, abstractmethod
class Persona(ABC):
    @classmethod
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre  
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    @abstractmethod
    def actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre}, mi edad es {self.edad} y trabajo de {self.actividad}")
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad, carrera):
        super.__init__(nombre, edad, sexo, actividad)

    def actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
        
class Tranajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad, salario):
        super.__init__(nombre, edad, sexo, actividad)
        self.salario=salario
    
    def actividad(self):
        print(f"Estoy trabajando de: {self.actividad}")
        