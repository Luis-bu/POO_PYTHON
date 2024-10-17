class Persona():
    #Atributos privados
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_edad(self):
       return self.edad
    
    def set_edad(self, edad):
        self.edad = edad
    
persona1 = Persona("Luis", 17)

persona1.set_edad(18)

print(persona1.get_nombre())
print(persona1.get_edad())