# ======================================================================
# CLASE SistemaDomotico
# Abstracción: Representa las reglas de control de las luces.
# Encapsulamiento: Contiene el estado de las luces (encendidas/apagadas)
# y la lógica para actualizar dicho estado.
# ======================================================================
class SistemaDomotico:
    def __init__(self):
        """
        Método constructor del sistema.
        Las luces inician apagadas por defecto.
        """
        self.luces_encendidas = False

    def actualizar_estado(self, es_de_noche, hay_movimiento):
        """
        Método que actualiza el estado de las luces según las condiciones.
        Parámetros: es_de_noche (booleano), hay_movimiento (booleano)
        """
        if es_de_noche and hay_movimiento:
            self.luces_encendidas = True
        else:
            self.luces_encendidas = False

    def obtener_estado_luces(self):
        """
        Método que devuelve un mensaje con el estado actual de las luces.
        Retorno: Un string indicando si las luces están ON u OFF.
        """
        if self.luces_encendidas:
            return "Luces ENCENDIDAS"
        else:
            return "Luces APAGADAS"

# ======================================================================
# CLASE SimuladorCasa
# Gestiona el flujo de la simulación y la interacción con el usuario.
# ======================================================================
class SimuladorCasa:
    def __init__(self):
        """
        Constructor que crea una instancia del SistemaDomotico.
        """
        self.sistema_luces = SistemaDomotico()

    def iniciar_simulacion(self):
        """
        Método que contiene el bucle principal para simular
        las condiciones de la casa y controlar las luces.
        """
        print("Iniciando Simulador de Casa Inteligente ")

        while True:
            # 1. Simular las condiciones (pedir datos al usuario)
            es_noche = input("\n¿Es de noche? (si/no): ").strip().lower() == "si"
            hay_movimiento = input("¿Hay movimiento? (si/no): ").strip().lower() == "si"

            # 2. Llamar al método del objeto 'sistema_luces' para que actualice su estado
            self.sistema_luces.actualizar_estado(es_noche, hay_movimiento)

            # 3. Obtener y mostrar el estado actual de las luces
            estado_actual = self.sistema_luces.obtener_estado_luces()
            print(f"-> Estado del sistema: {estado_actual}")
            
            # 4. Preguntar al usuario si desea continuar la simulación
            continuar = input("\n¿Continuar simulación? (si/no): ").strip().lower()
            if continuar != "si":
                break
        
        print("\nApagando el simulador. ¡Hasta luego!")


# ======================================================================
# ZONA DE CÓDIGO PRINCIPAL
# ======================================================================
if __name__ == "__main__":
    # 1. Creamos un objeto de la clase SimuladorCasa.
    simulador = SimuladorCasa()
    
    # 2. Llamamos al método 'iniciar_simulacion' para comenzar.
    simulador.iniciar_simulacion()