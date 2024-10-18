class Company():
    def __init__ (self):
        self.empleados=[]
        
    def add_employee(self, empleado):
         self.empleados.append(empleado)
         print("Empleado añadido correctamente")
    
    def remove_employee(self,nombre):
        for empleado in self.empleados:
            if nombre == empleado.name:
                self.empleados.remove(empleado)
                print("Empleado eliminado correctamente")
        else: print("Empleado no encontrado")
        
    def list_employees(self):
        print("Lista de empleados: ")
        for empleado in self.empleados:
            print(f"{empleado}\n")
    
    def promote_employees(self, nombre):
        for empleado in self.empleados:
            if nombre == empleado.name:
                empleado.promote()
    
    def give_bonus_to_employee(self, nombre):
        for empleado in self.empleados:
            if nombre == empleado.name:
              empleado.give_bonus()
                 