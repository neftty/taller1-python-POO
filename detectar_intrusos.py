# CLASE Alarma

class Alarma:
    def __init__(self):
        self.activada = False

    def activar(self):
        self.activada = True
        print("La alarma ha sido ACTIVADA.")

    def desactivar(self):
        self.activada = False
        print("La alarma ha sido DESACTIVADA.")

# CLASE PanelDeControl

class PanelDeControl:
    def __init__(self):
        self.alarma = Alarma()

    def simular_sensores(self):
        # Verificamos si la alarma está activada antes de hacer nada.
        if not self.alarma.activada:
            print("\nAVISO: La alarma está desactivada. No se detectarán intrusos.")
            print("Por favor, active la alarma desde el menú para comenzar la simulación.")
            return

        print("\n--- Iniciando Simulación de Sensores ---")

        # Preguntar si es de noche
        respuesta = input("¿Es de noche? (si/no): ").lower()
        es_de_noche = respuesta == "si"

        # Lectura de los sensores
        lecturas = []
        print("\nIngrese el estado de los 3 sensores (1=movimiento, 0=no):")
        for i in range(3):
            valor = int(input("   Sensor " + str(i + 1) + ": "))
            while valor != 0 and valor != 1:
                print("Error: Ingrese solo 1 o 0.")
                valor = int(input("   Sensor " + str(i + 1) + ": "))
            lecturas.append(valor)

        # Contar cuántos sensores detectaron movimiento
        sensores_con_movimiento = 0
        for lectura in lecturas:
            if lectura == 1:
                sensores_con_movimiento += 1

        # Regla de activación de alarma
        print("\n--- RESULTADO ---")
        if sensores_con_movimiento >= 2 and es_de_noche:
            print("¡ALARMA ACTIVADA! Se detectó un posible intruso.")
        else:
            print("Todo en calma. No se activa la alarma.")

    def iniciar_menu(self):
        print("Sistema de Detección de Intrusos")
        while True:
            print("\n--- MENÚ ---")
            print("1. Activar Alarma")
            print("2. Desactivar Alarma")
            print("3. Simular Lectura de Sensores")
            print("4. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.alarma.activar()
            elif opcion == "2":
                self.alarma.desactivar()
            elif opcion == "3":
                self.simular_sensores()
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")

        print("\nApagando el sistema. ¡Adiós!")

# -------------------- CÓDIGO PRINCIPAL --------------------
panel = PanelDeControl()
panel.iniciar_menu()
