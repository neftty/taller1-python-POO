# ======================================================================
# CLASE SistemaAcceso
# Abstracción: Representa las reglas de acceso a la tienda.
# Encapsulamiento: Contiene la lógica para decidir si se permite
# o deniega el acceso.
# ======================================================================
class SistemaAcceso:
    def verificar_acceso(self, tiene_membresia, en_horario, es_empleado):
        """
        Método que aplica las reglas de acceso.
        Parámetros: tiene_membresia, en_horario, es_empleado (todos booleanos)
        Retorno: Un string con el resultado del control de acceso.
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

# ======================================================================
# CLASE TerminalAcceso
# Gestiona el flujo de la simulación y la interacción con el usuario.
# ======================================================================
class TerminalAcceso:
    def __init__(self):
        """
        Constructor que crea una instancia del SistemaAcceso.
        """
        self.sistema = SistemaAcceso()

    def iniciar_operacion(self):
        """
        Método que contiene el bucle principal para simular
        los intentos de acceso a la tienda.
        """
        print("Iniciando Terminal de Control de Acceso")

        while True:
            # 1. Recopilar la información del usuario
            print("\n--- Verificando Acceso ---")
            membresia = input("¿El cliente tiene membresía? (si/no): ").strip().lower() == "si"
            horario = input("¿Está dentro del horario de atención? (si/no): ").strip().lower() == "si"
            empleado = input("¿La persona es un empleado? (si/no): ").strip().lower() == "si"

            # 2. Llamar al método del objeto 'sistema' para que evalúe las condiciones
            resultado = self.sistema.verificar_acceso(membresia, horario, empleado)

            # 3. Mostrar el resultado
            print(f"-> Resultado: {resultado}")
            
            # 4. Preguntar al usuario si desea continuar
            continuar = input("\n¿Verificar a otra persona? (si/no): ").strip().lower()
            if continuar != "si":
                break
        
        print("\nApagando la terminal. ¡Hasta luego! ")


# ======================================================================
# ZONA DE CÓDIGO PRINCIPAL
# ======================================================================
if __name__ == "__main__":
    # 1. Creamos un objeto de la clase TerminalAcceso.
    terminal = TerminalAcceso()
    
    # 2. Llamamos al método 'iniciar_operacion' para comenzar.
    terminal.iniciar_operacion()