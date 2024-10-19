def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
        print("Despues de llamar a la función")
    return funcion_modificada
    
@decorador
def saludo():
    print("Hola mundo")

saludo()