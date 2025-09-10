# ======================================================================
# CLASE FizzBuzzJuego (Esta clase no necesita cambios)
# ======================================================================
class FizzBuzzJuego:
    def obtener_resultado(self, numero):
        """
        Método que aplica las reglas de FizzBuzz a un número.
        """
        if numero % 15 == 0:
            return "FizzBuzz"
        elif numero % 3 == 0:
            return "Fizz"
        elif numero % 5 == 0:
            return "Buzz"
        else:
            return str(numero)

# ======================================================================
# CLASE Aplicacion (Modificada para incluir el menú)
# ======================================================================
class Aplicacion:
    def __init__(self):
        """
        Método constructor de la aplicación.
        """
        self.juego = FizzBuzzJuego()

    def _resolver_ejercicio(self):
        """
        Método privado que contiene la lógica para ejecutar una
        ronda del juego FizzBuzz.
        """
        print("\n--- Resolviendo FizzBuzz ---")
        # Bucle para solicitar y validar la entrada del usuario.
        while True:
            try:
                limite_str = input("Introduce hasta qué número quieres jugar (entre 1 y 100): ")
                limite = int(limite_str)
                
                # Validamos que el número esté DENTRO del rango de 1 a 100.
                if 1 <= limite <= 100:
                    break  # Si el número es válido, rompemos el bucle.
                else:
                    print("Error: El número debe estar entre 1 y 100.")

            except ValueError:
                print("Error: Debes introducir un número entero válido.")

        print(f"\n--- Resultado de FizzBuzz hasta {limite} ---\n")

        # Bucle que recorre los números desde 1 hasta el límite.
        for numero_actual in range(1, limite + 1):
            resultado = self.juego.obtener_resultado(numero_actual)
            print(resultado)
        
        print("\n--- ¡Ejercicio Terminado! ---")
        input("Presiona Enter para volver al menú...")

    def iniciar(self):
        """
        Método principal que muestra el menú y gestiona las opciones del usuario.
        """
        # Mensaje de bienvenida que explica el problema.
        print("¡Bienvenido al Desafío FizzBuzz!")
        print("El programa recorrerá los números desde 1 hasta el número que elijas.")
        print("Imprimirá 'Fizz' para múltiplos de 3, 'Buzz' para múltiplos de 5,")
        print("y 'FizzBuzz' para múltiplos de ambos.")

        # Bucle principal del menú.
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Resolver Ejercicio FizzBuzz")
            print("2. Salir")
            
            opcion = input("Elige una opción: ")

            if opcion == "1":
                # La opción 1 llama al método para resolver el ejercicio.
                # Al terminar, volverá automáticamente a este menú.
                self._resolver_ejercicio()
            elif opcion == "2":
                # La opción 2 rompe el bucle y termina el programa.
                print("\n¡Gracias por jugar! Adiós.")
                break
            else:
                print("Opción no válida. Por favor, elige 1 o 2.")

# ======================================================================
# ZONA DE CÓDIGO PRINCIPAL
# ======================================================================
if __name__ == "__main__":
    app = Aplicacion()
    app.iniciar()
