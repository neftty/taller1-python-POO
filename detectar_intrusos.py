# ======================================================================
# CLASE SistemaSeguridad
# Abstracción: Representa el sistema de seguridad con sus reglas.
# Encapsulamiento: Contiene el estado (armado/desarmado) y la lógica
# para verificar los sensores.
# ======================================================================
class SistemaSeguridad:
    def __init__(self):
        """
        Método constructor del sistema.
        Por defecto, el sistema inicia desarmado.
        """
        self.armado = False

    def armar(self):
        """Método para activar el sistema."""
        self.armado = True
        print("Sistema de seguridad ARMADO.")

    def desarmar(self):
        """Método para desactivar el sistema."""
        self.armado = False
        print("Sistema de seguridad DESARMADO.")

    def verificar_sensores(self, lecturas_sensores, es_de_noche):
        """
        Método que aplica las reglas de seguridad.
        Parámetros: lecturas_sensores (lista), es_de_noche (booleano)
        Retorno: Un string con el estado de la alarma.
        """
        # Si el sistema no está armado, no hace nada.
        if not self.armado:
            return "Sistema desarmado. Todo en calma."

        # sum() cuenta los '1' en la lista. Si hay 2 o más, es True.
        movimiento_detectado = sum(lecturas_sensores) >= 2
        
        # La alarma solo se activa si se cumplen AMBAS condiciones.
        if movimiento_detectado and es_de_noche:
            return "¡ALERTA! Intruso detectado. Alarma activada. "
        else:
            return "Todo en calma."

# ======================================================================
# CLASE PanelControl
# Gestiona el menú, el flujo del programa y la interacción con el usuario.
# ======================================================================
class PanelControl:
    def __init__(self):
        """
        Constructor que crea una instancia del SistemaSeguridad.
        """
        self.sistema = SistemaSeguridad()

    def _iniciar_monitoreo(self):
        """
        Método privado que contiene el bucle para leer los sensores.
        """
        if not self.sistema.armado:
            print("\nADVERTENCIA: Debe armar el sistema antes de iniciar el monitoreo.")
            return

        print("\n--- Iniciando monitoreo ---")
        es_de_noche = input("¿Es de noche? (si/no): ").strip().lower() == "si"
        
        while True:
            try:
                lecturas = []
                print("\nIngrese el estado de los sensores (1=movimiento, 0=no):")
                for i in range(3):
                    valor = int(input(f"  Sensor {i+1}: "))
                    lecturas.append(valor)
                
                # Llamamos al método de nuestro objeto 'sistema' para que evalúe.
                estado = self.sistema.verificar_sensores(lecturas, es_de_noche)
                print(f"-> Estado: {estado}")

            except ValueError:
                print("Error: Ingrese solo 1 o 0.")
            
            continuar = input("\n¿Revisar sensores de nuevo? (si/no): ").strip().lower()
            if continuar != "si":
                break

    def iniciar(self):
        """
        Método principal que muestra el menú y gestiona las opciones.
        """
        print("Panel de Control del Sistema de Seguridad")
        while True:
            print("\n--- MENÚ ---")
            print("1. Armar sistema")
            print("2. Desarmar sistema")
            print("3. Iniciar monitoreo")
            print("4. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.sistema.armar()
            elif opcion == "2":
                self.sistema.desarmar()
            elif opcion == "3":
                self._iniciar_monitoreo()
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")
        
        print("\n🔌 Apagando el panel de control. ¡Hasta luego! ")

# ======================================================================
# ZONA DE CÓDIGO PRINCIPAL
# ======================================================================
if __name__ == "__main__":
    panel = PanelControl()
    panel.iniciar()