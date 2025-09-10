# Programación Orientada a Objetos en Python
# Temas: Herencia, Polimorfismo, Encapsulamiento, Abstracción

# Clase principal Carro
class Carro:
    def __init__(self, marca, modelo, color):
        self.dato_marca = marca
        self.dato_modelo = modelo
        self.dato_color = color

    # Métodos Setters
    def set_marca(self, nueva_marca):
        self.dato_marca = nueva_marca

    def set_modelo(self, nuevo_modelo):
        self.dato_modelo = nuevo_modelo

    def set_color(self, nuevo_color):
        self.dato_color = nuevo_color

    # Métodos Getters
    def get_marca(self):
        return self.dato_marca

    def get_modelo(self):
        return self.dato_modelo

    def get_color(self):
        return self.dato_color

    # Método para imprimir información
    def imprimir_carro(self):
        print(self.dato_marca + " " + self.dato_modelo + " " + self.dato_color)

    # Dependencia de otro objeto
    def mover_carro(self, obj_motor):
        obj_motor.prender_motor()

    def apagar_carro(self, obj_motor):
        obj_motor.apagar_motor()


# Clase Motor
class Motor:
    def __init__(self):
        self.estado_motor = None

    def prender_motor(self):
        self.estado_motor = "Prendido"
        print("Motor encendido.")

    def apagar_motor(self):
        self.estado_motor = "Apagado"
        print("Motor apagado.")


# Clase Lista de carros
class ListaCarro:
    def __init__(self):
        self.lista_carros = []

    def agregar_carro(self, carro):
        self.lista_carros.append(carro)

    def mostrar_carros(self):
        for carro in self.lista_carros:
            carro.imprimir_carro()


# Zona de código principal
    obj_carro = Carro("Mazda", "2001", "Negro")
    dato_marca = obj_carro.get_marca()
    print("Marca del carro: " + dato_marca)

    obj_carro.set_marca("Ford")
    obj_carro.imprimir_carro()

    obj_motor = Motor()
    obj_carro.mover_carro(obj_motor)  # Agregación
    obj_carro.apagar_carro(obj_motor)
