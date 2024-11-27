#LSP (Principio )

#En ave ponemos aquello que absolutamente TODAS las aves deben poder hacer
class Ave:
    pass 

#Usamos la herencia para poder crear distintos elementos
class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"


class AveNoVoladora(Ave):
    pass