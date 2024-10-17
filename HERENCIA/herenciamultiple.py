#Creamos la clase persona para tener un molder para cualquiera usuario
class Persona:
    #Constructor
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    #Método de cualquier persona
    def hablar(self):
        print(f"{self.nombre} esta hablando")    

#Creamos la clase artista que tiene un únio atributo
class Artista():
    #Constructor 
    def __init__(self, habilidad):
        self.habilidad=habilidad
        
    
#Herencia multiple

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, trabajo, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.trabajo=trabajo
        self.salario=salario
    #Llama un método propio de el mismo con (self)
    def presentarse(self):
        return f"Hola, soy {self.nombre}, soy de nacionalidad {self.nacionalidad} y {self.decir_su_habilidad()}"
    
    def decir_su_habilidad(self):
        return f"mi habilidad es: {self.habilidad}"
        
#Empleado ha heredado tanto los atributos como los métodos
Pedro=EmpleadoArtista("Pedro", 52, "Colombiana", "Pintar", "Artista", 1500)


print(Pedro.presentarse())
Pedro.hablar()

#Saber si una clase hereda de otra (bool)
herencia = issubclass(EmpleadoArtista, Artista)
print(herencia)
#Saber si un objeto es instancia de una clase
instancia = isinstance(Pedro, EmpleadoArtista)
print(herencia)