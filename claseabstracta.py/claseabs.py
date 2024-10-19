from abc import ABC, abstractmethod
class Persona(ABC):
    #Hacemos que sea una clase de tipo abstracta
    @classmethod
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre  
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    #Método abstracto
    @abstractmethod
    def hacer_actividad(self):
        pass
    
    #Método NO abstracto
    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre}, mi edad es {self.edad} y me gusta {self.actividad}")
    
#Estudiante hereda de la clase abstracta
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        return f"Estoy estudiando {self.actividad}"
    
    def actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad, salario):
        super().__init__(nombre, edad, sexo, actividad)
        self.salario=salario
    
    def hacer_actividad(self):   
        return f"{self.nombre} esta haciendo su trabajo de {self.actividad}"
    
        
juan = Trabajador("Juan", 24, "No binario", "Programador", 100000)

juan.presentarse()
print(juan.hacer_actividad())

pedro = Estudiante("Pedro", 18, "Masculino", "Cantar")
pedro.presentarse()
print(pedro.hacer_actividad())