#OCP (Principio de <abierto/cerrado>)
#Debemos tener un codigo apto para añadir, pero no para modificar

#No queremos modificar nuestra clase
class Notificador():
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError

#Añadimos la funcionalidad de enviar una notificación por Email
class NotificadorEmail(Notificador):
    def notificar(self):
        
        #Asumimos que usuario es un objeto con mail, numero, sms etc...
        print(f"Enviando mensaje a {self.usuario.email}")

#De esta forma no cambiamos la clase original
class NotidicadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")