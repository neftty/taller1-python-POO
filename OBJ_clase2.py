class saludo:
    #metodo constructor 
    #se usa para iniciar obj
    def __init__(self, dato_texto):
        self.mensaje=dato_texto 
        print(self.mensaje)
    
    def toma_nombre(self):
        nombre_usuario=input("escriba el nombre del usuario: ")
        return nombre_usuario
    
    def hacer_mensaje(self, dato_usuario):
        self.mensaje="hola usuario"+dato_usuario
        self.imprimir_mensaje(self.mensaje)

    def get_mensaje(self): #29
        return self.mensaje
    
    def set_mensaje(self, dato_usuario):
        self.mensaje="hola  "+dato_usuario
        self.imprimir_mensaje(self.mensaje)
    
    def imprimir_mensaje(self, dato_mensaje):
        print(dato_mensaje)
#--------------------codigo principal----------------------
#tener llevar y retornar
texto="hola usuario"
obj_mensaje=saludo(texto)
nombre=obj_mensaje.toma_nombre()
obj_mensaje.hacer_mensaje(nombre)
#obj_mensaje.imprimir_mensaje(texto)

























    

