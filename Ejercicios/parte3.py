import random
class luchador():
    def __init__(self, nombre, nivel_poder, habilidad):
        self.nombre = nombre
        self.nivel_poder = nivel_poder
        self.habilidad = habilidad
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nNivel de poder: {self.nivel_poder}\nHabilidad: {self.habilidad}"
    
    def __add__(self, other):
        nuevo_nombre= f"{self. nombre} {other.nombre}"
        nuevo_nivel_poder = self.nivel_poder + other.nivel_poder
        nueva_habilidad = random.choice([self.habilidad, other.habilidad, f"{self.habilidad} y {other.habilidad}"])
        return luchador(nuevo_nombre,nuevo_nivel_poder,nueva_habilidad)
    
p1 = luchador("Ryu", 9, "Hadouken")
p2 = luchador("Chun-li",8, "Hyakuretsukyaku")
p3 = luchador("Ken Masters", 9, "Shoryuken")
p4 = luchador("Guile", 7, "Sonic boom")

print(p1+p3)