# CLASE Climatizador

class Climatizador:
    def __init__(self):
        # El aire acondicionado inicia apagado por defecto.
        self.ac_encendido = False

    def actualizar_estado(self, temperatura, humedad):
        # Actualiza el estado del AC según las condiciones.
        condicion1 = temperatura > 28 and humedad > 60
        condicion2 = temperatura > 30
        
        if condicion1 or condicion2:
            self.ac_encendido = True
        else:
            self.ac_encendido = False

    def obtener_estado_ac(self):
        # Devuelve un mensaje con el estado actual del AC.
        if self.ac_encendido:
            return "Aire Acondicionado ENCENDIDO"
        else:
            return "Aire Acondicionado APAGADO"

# CLASE SimuladorAmbiente

class SimuladorAmbiente:
    def __init__(self):
        # Creamos una instancia del Climatizador.
        self.climatizador = Climatizador()

    def iniciar_simulacion(self):
        """
        Método que contiene el bucle principal de la simulación.
        """
        print("Iniciando Simulador de Aire Acondicionado")

        while True:
            #  Simular la lectura de sensores (pedir datos al usuario).
            temp_str = input("\nIngrese la temperatura actual (°C): ")
            temp = float(temp_str)
            
            humedad_str = input("Ingrese la humedad actual (%): ")
            humedad = float(humedad_str)

            self.climatizador.actualizar_estado(temp, humedad)

            estado_actual = self.climatizador.obtener_estado_ac()
            print("-> Estado del sistema: " + estado_actual)
            
            continuar = input("\n¿Continuar simulación? (si/no): ").lower()
            if continuar != "si":
                break
        
        print("\nApagando el simulador. ¡Hasta luego!")


#CÓDIGO PRINCIPAL

#Creamos un objeto de la clase SimuladorAmbiente.
simulador = SimuladorAmbiente()

#  Llamamos al método 'iniciar_simulacion' para comenzar.
simulador.iniciar_simulacion()

