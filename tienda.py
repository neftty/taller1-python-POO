# CLASE SistemaAcceso

class SistemaAcceso:
    def verificar_acceso(self, tiene_membresia, en_horario, es_empleado):
        """
        Método que aplica las reglas de acceso.
        """
        # Condición 1: El cliente tiene membresía Y es horario de atención.
        condicion_cliente = tiene_membresia and en_horario
        # Condición 2: La persona es un empleado.
        condicion_empleado = es_empleado
        
        # Si se cumple CUALQUIERA de las dos condiciones, se permite el acceso.
        if condicion_cliente or condicion_empleado:
            return "Acceso Permitido"
        else:
            return "Acceso Denegado"

# CLASE TerminalAcceso

class TerminalAcceso:
    def __init__(self):
        # Creamos una instancia del SistemaAcceso.
        self.sistema = SistemaAcceso()

    def iniciar_operacion(self):
        """
        Método que contiene el bucle principal de la simulación.
        """
        print("Iniciando Terminal de Control de Acceso")

        while True:
            # 1. Recopilar la información del usuario de forma explícita
            print("\n--- Verificando Acceso ---")
            
            # Pregunta 1: Membresía
            respuesta_membresia = input("¿El cliente tiene membresía? (si/no): ").lower()
            if respuesta_membresia == "si":
                membresia = True
            else:
                membresia = False

            # Pregunta 2: Horario
            respuesta_horario = input("¿Está dentro del horario de atención? (si/no): ").lower()
            if respuesta_horario == "si":
                horario = True
            else:
                horario = False

            # Pregunta 3: Empleado
            respuesta_empleado = input("¿La persona es un empleado? (si/no): ").lower()
            if respuesta_empleado == "si":
                empleado = True
            else:
                empleado = False

            resultado = self.sistema.verificar_acceso(membresia, horario, empleado)

            print("-> Resultado: " + resultado)
            
            continuar = input("\n¿Verificar a otra persona? (si/no): ").lower()
            if continuar != "si":
                break
        
        print("\nApagando la terminal. ¡Hasta luego!")


#--------------------CÓDIGO PRINCIPAL----------------------

# 1. Creamos un objeto de la clase TerminalAcceso.
terminal = TerminalAcceso()

# 2. Llamamos al método 'iniciar_operacion' para comenzar.
terminal.iniciar_operacion()
