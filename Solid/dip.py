#DIP (Principio de inmersión de dependencias)

# class Diccionario():
#     def verificar_palabra(self, palabra):
#         pass
        
# class CorrectorOrtográfico():
#     def __init__(self):
#         self.diccionario=Diccionario
    
#     def corregir_texto(self, texto):
    
from abc import abstractmethod

class VerificadorOrtografico():
   @abstractmethod
   def verificar_palabra(self, palabra):
       pass

class Diccionario(VerificadorOrtografico):
     def verificar_palabra(self, palabra):
         pass