
class A:
    def hablar(self):
        print("Hola mundo A")
        
class B(A):
    def hablar(self):
        print("Hola mundo B")        
        
class C(A):
    def hablar(self):
        print("Hola mundo C")        
        
class D(B,C):
    def hablar(self):
        print("Hola mundo D")
        A.hablar(self)
  
#Instanciamos
d=D()
d.hablar()
print(D.mro())
C.hablar(d)