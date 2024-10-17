class Miclase():
    #Con "_" al inicio, se aclará que es un atributo privado
    def __init__(self):
        self.__atributo = "Valor"
    #Metodo privado
    
    def __hablar(self):
        print("Hablando")
    
objeto = Miclase()
print(objeto.__atributo)
print(objeto.__hablar)