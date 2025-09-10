# CLASE Sala
class Sala:
    # El método constructor. Se ejecuta cuando creamos una nueva sala.
    def __init__(self, capacidad):
        self.capacidad_total = capacidad
    
        self.asientos = []
        for _ in range(capacidad):
            self.asientos.append(False)

    # Método para mostrar el estado de todos los asientos
    def mostrar_asientos(self):
        print("--- Estado de los Asientos ---")
        for i in range(self.capacidad_total):
            numero_de_asiento = i + 1
            
            if self.asientos[i] == True:
                estado = "[Ocupado]"
            else:
                estado = "[Libre]"
            
            print("Asiento " + str(numero_de_asiento) + ": " + estado)

    # Método para intentar reservar un asiento específico
    def reservar_asiento(self, numero_asiento):
        indice = numero_asiento - 1
        
        # 1. Validar si el número de asiento es válido 
        if indice < 0 or indice >= self.capacidad_total:
            print("Error: Ese número de asiento no existe.")
            return False # Retornamos False para indicar que la reserva falló

        # 2. Validar si el asiento ya está ocupado
        if self.asientos[indice] == True:
            print("Error: Lo sentimos, ese asiento ya está ocupado.")
            return False # Retornamos False para indicar que la reserva falló

        # Si pasamos las validaciones, reservamos el asiento
        self.asientos[indice] = True
        print("¡Reserva realizada con éxito para el asiento " + str(numero_asiento) + "!")
        return True # Retornamos True para indicar que la reserva fue exitosa

    # Método para saber si la sala ya está llena
    def esta_llena(self):
        if False not in self.asientos:
            return True
        else:
            return False



# CLASE SistemaDeReservas

class SistemaDeReservas:
    def __init__(self):
        self.sala = Sala(10)

    # Método principal que inicia el programa
    def iniciar(self):
        print("Bienvenido al Sistema de Reservas del Cine")

        while self.sala.esta_llena() == False:
            
            self.sala.mostrar_asientos()
            
            opcion = input("\n¿Desea reservar un asiento? (escriba 'si' o 'no'): ")
            opcion = opcion.lower()

            if opcion == "si":
                try:
                    asiento_elegido = int(input("Por favor, ingrese el número de asiento que desea: "))
                    self.sala.reservar_asiento(asiento_elegido)
                
                except ValueError:
                    print("Error: Debe ingresar un número válido.")

            elif opcion == "no":
                print("Gracias por visitarnos. Saliendo del sistema...")
                break
            
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
            
            print("----------------------------------------") 

        print("\nLo sentimos, la sala está completa. ¡Gracias por usar el sistema!")


#CÓDIGO PRINCIPAL

#la variable sistema, ahora contiene un objeto 
sistema = SistemaDeReservas()

#ejecutar el método principal
sistema.iniciar()
