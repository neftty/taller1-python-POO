# CLASE ControlClima

class ControlClima:
    def decidir_accion(self, temperatura):
        """
        Método que evalúa la temperatura y decide una acción.
        """
        if temperatura < 10:
            return "Temperatura baja. Activando calefactor."
        elif 10 <= temperatura <= 25:
            return "Temperatura estable. Sistema inactivo."
        else: 
            return "Temperatura alta. Activando ventilador."

# CLASE SimuladorInvernadero

class SimuladorInvernadero:
    def __init__(self):
        # Creamos un objeto de la clase ControlClima.
        self.controlador = ControlClima()

    def iniciar_simulacion(self):
        """
        Método que contiene el bucle principal de la simulación.
        """
        print("Iniciando Sistema de Control de Invernadero")

        # Bucle principal del programa
        while True:
            temp_actual_str = input("\nIngrese la temperatura actual (°C): ")
            temp_actual = float(temp_actual_str)

            estado_del_sistema = self.controlador.decidir_accion(temp_actual)

            print("Estado: " + estado_del_sistema)
            
            continuar = input("\n¿Continuar simulación? (si/no): ").lower()
            if continuar != "si":
                break 
        
        print("\nApagando el sistema de control. ¡Hasta luego!")


#--------------------CÓDIGO PRINCIPAL----------------------

# 1. Creamos un objeto de la clase SimuladorInvernadero.
simulador = SimuladorInvernadero()

# 2. Llamamos al método que inicia la simulación.
simulador.iniciar_simulacion()
