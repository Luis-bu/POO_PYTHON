class Miclase():
    
    #Con "_" al inicio, se aclará que es un atributo privado
    def __init__(self, atributo):
        self.__atributo = atributo
        
    #Metodo privado
    def __hablar(self):
        return "Hablando..."
    
    #Con @property decimos que es un getter y nos sirve para acceder de forma falsa a un atributo
    @property
    def atributo(self):
        return self.__atributo
    
    #2 decoradores diferentes, ahora se puede cambiar la variable original al llamarla como este método
    @atributo.setter
    def atributo(self, new_atributo):
        self.__atributo = new_atributo
    
    #Ahora podemos borrar metodos o atributos
    @atributo.deleter
    def atributo(self):
        del self.__atributo
    
objeto = Miclase("Correr")

#Ahora podemos obtener el atributo real por medio del falso
print(objeto.atributo)


#Ahora podemos a traves del atributo falso "cambiar el original"
objeto.atributo = "Cantar"

print(objeto.atributo)

#Borramos a traves de la propiedad falsa, la original
del objeto.atributo

#Suelta error por que intentamos acceder a un elemento que no exite (lo borramos)
#print(objeto.atributo)
