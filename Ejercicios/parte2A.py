class Persona():
    def __init__(self, nombre, edad):
         self.nombre=nombre
         self.edad=edad
         
    def informacion(self):
        return f"El nombre es {self.nombre} y la edad es {self.edad} " 
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado=grado
    
    def sugrado(self):
        return f"el grado de {self.nombre} es {self.grado}"
    

estudiante1 = Estudiante("Ricardo", 18, 11)

print(estudiante1.informacion())
print(estudiante1.sugrado())