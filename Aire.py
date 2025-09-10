# ======================================================================
# CLASE Climatizador
# Abstracción: Representa las reglas de funcionamiento del aire acondicionado.
# Encapsulamiento: Contiene el estado (encendido/apagado) y la lógica
# para actualizar dicho estado según la temperatura y humedad.
# ======================================================================
class Climatizador:
    def __init__(self):
        """
        Método constructor del sistema.
        El aire acondicionado inicia apagado por defecto.
        """
        self.ac_encendido = False

    def actualizar_estado(self, temperatura, humedad):
        """
        Método que actualiza el estado del AC según las condiciones.
        Parámetros: temperatura (float), humedad (float)
        """
        # Condición 1: Temperatura > 28°C Y Humedad > 60%
        condicion1 = temperatura > 28 and humedad > 60
        # Condición 2: Temperatura > 30°C (independiente de la humedad)
        condicion2 = temperatura > 30
        
        # Si se cumple cualquiera de las dos condiciones, se enciende.
        if condicion1 or condicion2:
            self.ac_encendido = True
        else:
            self.ac_encendido = False

    def obtener_estado_ac(self):
        """
        Método que devuelve un mensaje con el estado actual del AC.
        Retorno: Un string indicando si el AC está ON u OFF.
        """
        if self.ac_encendido:
            return "Aire Acondicionado ENCENDIDO"
        else:
            return "Aire Acondicionado APAGADO"

# ======================================================================
# CLASE SimuladorAmbiente
# Gestiona el flujo de la simulación y la interacción con el usuario.
# ======================================================================
class SimuladorAmbiente:
    def __init__(self):
        """
        Constructor que crea una instancia del Climatizador.
        """
        self.climatizador = Climatizador()

    def iniciar_simulacion(self):
        """
        Método que contiene el bucle principal para simular
        las condiciones del ambiente y controlar el AC.
        """
        print("Iniciando Simulador de Aire Acondicionado")

        while True:
            try:
                # 1. Simular la lectura de sensores (pedir datos al usuario)
                temp = float(input("\nIngrese la temperatura actual (°C): "))
                humedad = float(input("Ingrese la humedad actual (%): "))

                # 2. Llamar al método del objeto 'climatizador' para que actualice su estado
                self.climatizador.actualizar_estado(temp, humedad)

                # 3. Obtener y mostrar el estado actual del AC
                estado_actual = self.climatizador.obtener_estado_ac()
                print(f"-> Estado del sistema: {estado_actual}")
            
            except ValueError:
                print("Error: Por favor, introduce valores numéricos válidos.")

            # 4. Preguntar al usuario si desea continuar la simulación
            continuar = input("\n¿Continuar simulación? (si/no): ").strip().lower()
            if continuar != "si":
                break
        
        print("\nApagando el simulador. ¡Hasta luego!")


# ======================================================================
# ZONA DE CÓDIGO PRINCIPAL
# ======================================================================
if __name__ == "__main__":
    # 1. Creamos un objeto de la clase SimuladorAmbiente.
    simulador = SimuladorAmbiente()
    
    # 2. Llamamos al método 'iniciar_simulacion' para comenzar.
    simulador.iniciar_simulacion()