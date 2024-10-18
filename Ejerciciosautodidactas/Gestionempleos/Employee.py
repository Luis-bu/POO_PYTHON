
class Employee():
    def __init__(self, name, position, salary):
        self.name=name
        self.position=position
        self.salary=salary
     
    def __str__(self):
        return f"Nuestro empleado: {self.name}\nOcupa el cargo de {self.position}\nY gana un salario de {self.salary} Wow!!!"    
        
    def promote(self):
        if self.position == "trabajador":
            self.position="empleado destacado"
            self.salary=self.salary * 1.10
            print("Ascendido correctamente")
        
        elif self.position == "empleado destacado":
            self.position = "gerente"
            self.salary = self.salary * 1.25
            print("Ascendido correctamente")
        
        elif self.position == "gerente":
            self.position = "jefe"
            self.salary = self.salary * 1.40
            print("Ascendido correctamente")
        
        elif self.position == "jefe":
            print("Ya tiene el cargo más alto, felicidades!!!")
        
        else: print("Cargo no valido")
        
    def give_bonus(self):
        self.salary+=self.salary * 0.1
        print("Bono aplicado correctamente")