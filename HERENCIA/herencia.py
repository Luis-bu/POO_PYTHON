class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print(f"{self.nombre} esta hablando")    

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        #Que va a heredar de su clase padre?
        super().__init__(nombre, edad, nacionalidad)
        #Atributos propios de los empleados
        self.trabajo=trabajo
        self.salario=salario
    def hablar(self):
        return super().hablar()
    
