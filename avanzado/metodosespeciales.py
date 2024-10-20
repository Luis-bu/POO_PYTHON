import random
class persona():
    def __init__(self, nombre , edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        
    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nSexo: {self.sexo}"
    
    #Sirve para hacer una representación del objeto
    def __repr__(self):
        return f'Persona: ("{self.nombre}", {self.edad})'
    
   #Sobrecarga de metodos
   #Cuando sumamos 2 elementos
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return persona(self.nombre + " " + otro.nombre, nuevo_valor, random.choice([self.sexo, otro.sexo]))
   
luis = persona("Luis", 17, "Masculino")
Maria = persona("Maria paula", 19, "Femenino")

persona_nueva = luis + Maria
print(persona_nueva)




