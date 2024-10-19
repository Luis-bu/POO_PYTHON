import statistics
class Estudiante():
    def __init__(self, nombre, edad, id):
        self.__nombre = nombre
        self.__edad = edad
        self.__id = id
        self.__calificaciones = []
    
    def __str__(self):
        resultado = f"Nombre: {self.__nombre}\nEdad: {self.__edad}\nID: {self.__id}\n"
        if not self.__calificaciones:
            resultado += "No hay calificaciones"
        else:
            for calificacion in self.__calificaciones:
                resultado += ("------\n")
                resultado += (f"| {calificacion}|\n")
                resultado+= ("------\n")
        return resultado
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_edad(self):
        return self.__edad
    
    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad
    
    def get_id(self):
        return self.__id
    
    def set_id(self, nueva_id):
        self.__id = nueva_id
    
    def agregar_calificaciones(self, *cal):
        cal = list(cal)
        self.__calificaciones.extend(cal)
        
    def borrar_calificacion(self, indice):
        self.__calificaciones.pop(indice)
    
    def borrar_todas_las_calificaciones(self):
        self.__calificaciones.clear()   
    
    def promedio(self):
        print(f"El promedio de las notas de {self.get_nombre()} es de: {statistics.mean(self.__calificaciones)}")
        
class Curso():
    def __init__(self, estudiantes):
        self.estudiantes = []
    

    def agregar_estudiante(self, nuevo_estudiante):
        self.estudiantes.append(nuevo_estudiante)
        print("Estudiante agregado correctamente")
    
    def eliminar_estudiante(self, id):
        encontrado, estudiante = self.__buscar_estudiante(id)
        if encontrado:
            self.estudiantes.remove(estudiante)
            print("Estudiante removido correctamente")
        else: print("Estudiante no encontrado")
        
    def __buscar_estudiante(self, id):
        for estudiante in self.estudiantes:
            if estudiante.get_id()==id:
                return (True, estudiante)
        return (False, None)
    
    def coincidir(self, id):
        encontrado, estudiante = self.__buscar_estudiante(id)
        if encontrado:
            print("Estudiante encontrado")
            estudiante.__str__()
        else: print("Estudiante no encontrado")

    def mostrar_todos_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante)
        
class Universidad():
    def __init__(self, id):
        self.id=id
        self.__cursos= []
    
    def agregar_curso(self, nuevo_curso):
        self.__cursos.append(nuevo_curso)
        print("Curso agregado correctamente")
           
    def eliminar_curso(self, id):
        for curso in self.__cursos:
            if curso.id==id:
                self.__cursos.remove(curso)
            else: print("Curso no encontrado")
    
    def mostrar_cursos(self):
        for curso in self.__cursos:
            curso.__str__()
        
            