class Estudiante():
    #Constructor para crear Estudiantes
    def __init__(self, nombre, edad, grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado 
    
    #Método estudiar
    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando")

#Preguntamos al usuario los datos de nuestro objeto 
nombre=input("Ingrese el nombre:\n")
edad=input("Ingresa la edad:\n")
grado=input("Ingresa el grado:\n")

estudiante1=Estudiante(nombre,edad,grado)

#Bucle para saber que quiere hacer el usuario
while True:
    accion=input("Que desea hacer:\n")
    if accion.lower()=="estudiar":
        estudiante1.estudiar()
    elif accion.lower()=="salir":
        print("Hasta luego!")
        break
    else:
        print("Accion no válida")