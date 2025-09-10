# 
# CLASE Sala
# 
class Sala:
    def __init__(self, filas, columnas):
        """
        Método constructor de la sala.
        Crea el atributo 'asientos' usando bucles 'for' para mayor claridad.
        """
        self.filas = filas
        self.columnas = columnas
        
        # --- Versión paso a paso para crear la sala ---
        # 1. Creamos una lista vacía que contendrá toda la sala.
        sala_completa = []
        # 2. Bucle exterior para cada fila.
        for _ in range(filas):
            # 3. Creamos una lista vacía para la fila actual.
            nueva_fila = []
            # 4. Bucle interior para cada asiento en la fila.
            for _ in range(columnas):
                # 5. Agregamos un asiento libre (False).
                nueva_fila.append(False)
            # 6. Agregamos la fila completa a la sala.
            sala_completa.append(nueva_fila)
        
        # 7. Asignamos la sala recién creada al atributo del objeto.
        self.asientos = sala_completa
        # --- Fin de la versión paso a paso ---

    def mostrar(self):
        """
        Método para imprimir el estado actual de la sala.
        """
        print("\nMapa de la sala (O = libre, X = reservado):")
        print("  ", end="")
        for i in range(self.columnas):
            print(f"{i}", end=" ")
        print()

        for i, fila in enumerate(self.asientos):
            print(f"{i} ", end="")
            for asiento in fila:
                print("X" if asiento else "O", end=" ")
            print()

    def reservar(self, fila, col):
        """
        Método para reservar un asiento.
        Retorna: True si la reserva fue exitosa, False si no lo fue.
        """
        if not (0 <= fila < self.filas and 0 <= col < self.columnas):
            print("Posición inválida. Por favor, intenta de nuevo.")
            return False
        
        if self.asientos[fila][col]:
            print("Lo sentimos, ese asiento ya está reservado.")
            return False
        
        self.asientos[fila][col] = True
        print("¡Reserva realizada con éxito!")
        return True

# 
# CLASE SistemaReservas
# 
class SistemaReservas:
    def __init__(self, filas, columnas):
        """
        Método constructor del sistema.
        """
        self.sala = Sala(filas, columnas)
        self.disponibles = filas * columnas

    def iniciar(self):
        """
        Método que contiene el bucle principal del programa.
        """
        print("Bienvenido al Sistema de Reservas de Cine")

        while self.disponibles > 0:
            self.sala.mostrar()
            print(f"\nAsientos disponibles: {self.disponibles}")

            opcion = input("¿Desea reservar un asiento? (si/no): ").strip().lower()

            if opcion == "si":
                try:
                    fila_reserva = int(input(f"Ingrese el número de fila: "))
                    col_reserva = int(input(f"Ingrese el número de columna: "))
                    
                    if self.sala.reservar(fila_reserva, col_reserva):
                        self.disponibles -= 1
                except ValueError:
                    print("Error: Debes ingresar solo números. Intenta de nuevo.")
            
            elif opcion == "no":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida, por favor escribe 'si' o 'no'.")
        
        print("\nGracias por usar el sistema. ¡Disfruta la función! ")


# ======================================================================
# ZONA DE CÓDIGO PRINCIPAL
# ======================================================================
if __name__ == "__main__":
    sistema = SistemaReservas(filas=5, columnas=6)
    sistema.iniciar()