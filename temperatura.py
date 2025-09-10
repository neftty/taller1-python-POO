# ======================================================================
# CLASE ControlClima
# Abstracción: Representa las reglas de control de temperatura.
# Encapsulamiento: Contiene el método con la lógica para decidir
# qué acción tomar según la temperatura.
# ======================================================================
class ControlClima:
    def decidir_accion(self, temperatura):
        """
        Método que evalúa la temperatura y decide una acción.
        Parámetro: temperatura
        Retorno: Un string con el estado del sistema.
        """
        if temperatura < 10:
            return "Temperatura baja. Activando calefactor"
        elif 10 <= temperatura <= 25:
            return "Temperatura estable. Sistema inactivo."
        else:  # Si es mayor que 25
            return "Temperatura alta. Activando ventilador"

# ======================================================================
# CLASE SimuladorInvernadero
# Gestiona el flujo de la simulación y la interacción con el usuario.
# ======================================================================
class SimuladorInvernadero:
    def __init__(self):
        """
        Método constructor del simulador.
        Crea un objeto de la clase ControlClima para usar su lógica.
        """
        self.controlador = ControlClima()

    def iniciar_simulacion(self):
        """
        Método que contiene el bucle principal para simular la
        lectura de temperatura y controlar el sistema.
        """
        print("Iniciando Sistema de Control de Invernadero")

        while True:
            try:
                # 1. Simular la lectura del sensor (pedir dato al usuario)
                temp_actual = float(input("\nIngrese la temperatura actual (°C): "))

                # 2. Llamar al método del objeto 'controlador' para obtener el estado
                estado_del_sistema = self.controlador.decidir_accion(temp_actual)

                # 3. Mostrar el estado actual del sistema
                print(f"-> Estado: {estado_del_sistema}")

            except ValueError:
                print("🚨 Error: Por favor, introduce un valor numérico válido para la temperatura.")
            
            # 4. Preguntar al usuario si desea continuar la simulación
            continuar = input("\n¿Continuar simulación? (si/no): ").strip().lower()
            if continuar != "si":
                break  # Romper el bucle si la respuesta no es "si"
        
        print("\nApagando el sistema de control. ¡Hasta luego!")


# ======================================================================
# ZONA DE CÓDIGO PRINCIPAL
# Aquí es donde el programa comienza a ejecutarse.
# ======================================================================
if __name__ == "__main__":
    # 1. Creamos un objeto (instancia) de la clase SimuladorInvernadero.
    simulador = SimuladorInvernadero()
    
    # 2. Llamamos al método 'iniciar_simulacion' para que comience la ejecución.
    simulador.iniciar_simulacion()