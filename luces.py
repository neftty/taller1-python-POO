# CLASE Sistema

class Sistema:
    def __init__(self):
        # Las luces inician apagadas por defecto.
        self.luces_encendidas = False

    def actualizar_estado(self, es_de_noche, hay_movimiento):
        # Actualiza el estado de las luces según las condiciones.
        if es_de_noche and hay_movimiento:
            self.luces_encendidas = True
        else:
            self.luces_encendidas = False

    def obtener_estado_luces(self):
        # Devuelve un mensaje con el estado actual de las luces.
        if self.luces_encendidas:
            return "Luces ENCENDIDAS"
        else:
            return "Luces APAGADAS"

# CLASE SimuladorCasa

class SimuladorCasa:
    def __init__(self):
        # Creamos una instancia del Sistema.
        self.sistema_luces = Sistema()

    def iniciar_simulacion(self):
        """
        Método que contiene el bucle principal de la simulación.
        """
        print("Iniciando Simulador de Casa Inteligente")

        while True:
            
            # Pregunta 1: ¿Es de noche?
            respuesta_noche = input("\n¿Es de noche? (si/no): ").lower()
            if respuesta_noche == "si":
                es_noche = True
            else:
                es_noche = False

            # Pregunta 2: ¿Hay movimiento?
            respuesta_movimiento = input("¿Hay movimiento? (si/no): ").lower()
            if respuesta_movimiento == "si":
                hay_movimiento = True
            else:
                hay_movimiento = False

            # 2. Llamar al método para que actualice su estado
            self.sistema_luces.actualizar_estado(es_noche, hay_movimiento)

            estado_actual = self.sistema_luces.obtener_estado_luces()
            print("-> Estado del sistema: " + estado_actual)
            
            continuar = input("\n¿Continuar simulación? (si/no): ").lower()
            if continuar != "si":
                break
        
        print("\nApagando el simulador. ¡Hasta luego!")


#--------------------CÓDIGO PRINCIPAL----------------------

# 1. Creamos un objeto de la clase SimuladorCasa.
simulador = SimuladorCasa()

# 2. Llamamos al método 'iniciar_simulacion' para comenzar.
simulador.iniciar_simulacion()
