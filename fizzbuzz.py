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
# CLASE Aplicacion (Aquí está la modificación)
# ======================================================================
class Aplicacion:
    def __init__(self):
        """
        Método constructor de la aplicación.
        """
        self.juego = FizzBuzzJuego()

    def iniciar(self):
        """
        Método que contiene el bucle principal del programa.
        """
        print("¡Bienvenido al Juego FizzBuzz!")

        limite = 0
        # Bucle para solicitar y validar la entrada del usuario.
        while True:
            try:
                limite_str = input("Introduce hasta qué número quieres jugar (entre 1 y 100): ")
                limite = int(limite_str)
                
                # --- MODIFICACIÓN AQUÍ ---
                # Validamos que el número esté DENTRO del rango de 1 a 100.
                if 1 <= limite <= 100:
                    break  # Si el número es válido, rompemos el bucle.
                else:
                    # Si está fuera del rango, mostramos un error específico.
                    print("Error: El número debe estar entre 1 y 100.")
                # --- FIN DE LA MODIFICACIÓN ---

            except ValueError:
                print("🚨 Error: Debes introducir un número entero válido.")

        print(f"\n--- Iniciando FizzBuzz hasta {limite} ---\n")

        # Bucle que recorre los números desde 1 hasta el límite.
        for numero_actual in range(1, limite + 1):
            resultado = self.juego.obtener_resultado(numero_actual)
            print(resultado)
        
        print("\n--- ¡Juego Terminado! ---")


# 
# ZONA DE CÓDIGO PRINCIPAL
# 
if __name__ == "__main__":
    app = Aplicacion()
    app.iniciar()