# ======================================================================
# CLASE Calculadora
# Abstracción: Representa las operaciones matemáticas básicas.
# Encapsulamiento: Contiene el método con la lógica para realizar
# los cálculos.
# ======================================================================
class Calculadora:
    def realizar_operacion(self, num1, num2, operacion):
        """
        Método que realiza un cálculo basado en la operación solicitada.
        Parámetros: num1, num2, operacion
        Retorno: El resultado del cálculo o un mensaje de error.
        """
        if operacion == "suma":
            return num1 + num2
        elif operacion == "resta":
            return num1 - num2
        elif operacion == "multiplicacion":
            return num1 * num2
        elif operacion == "division":
            # Manejo del caso especial de división por cero
            if num2 == 0:
                return "Error: No se puede dividir por cero"
            return num1 / num2
        else:
            return "Error: Operación no válida"

# ======================================================================
# CLASE Aplicacion
# Gestiona el flujo principal del programa y la interacción con el usuario.
# ======================================================================
class Aplicacion:
    def __init__(self):
        """
        Método constructor de la aplicación.
        Crea un objeto de la clase Calculadora para usar su lógica.
        """
        self.calculadora = Calculadora()

    def iniciar(self):
        """
        Método que contiene el bucle principal para que el usuario
        pueda realizar múltiples cálculos.
        """
        print("🧮 ¡Bienvenido a la Calculadora Simple! 🧮")

        while True:
            try:
                # 1. Pedir los datos al usuario
                num1 = float(input("\nIntroduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
                operacion = input("Elige la operación (suma, resta, multiplicacion, division): ").strip().lower()

                # 2. Llamar al método del objeto 'calculadora' para obtener el resultado
                resultado = self.calculadora.realizar_operacion(num1, num2, operacion)

                # 3. Mostrar el resultado
                print(f"👉 Resultado: {resultado}")

            except ValueError:
                print("🚨 Error: Debes introducir números válidos.")
            except Exception as e:
                print(f"Ha ocurrido un error inesperado: {e}")

            # 4. Preguntar al usuario si desea continuar
            continuar = input("\n¿Deseas realizar otro cálculo? (si/no): ").strip().lower()
            if continuar != "si":
                break  # Romper el bucle si la respuesta no es "si"
        
        print("\n¡Gracias por usar la calculadora! Adiós. 👋")


# ======================================================================
# ZONA DE CÓDIGO PRINCIPAL
# Aquí es donde el programa comienza a ejecutarse.
# ======================================================================
if __name__ == "__main__":
    # 1. Creamos un objeto (instancia) de la clase Aplicacion.
    app = Aplicacion()
    
    # 2. Llamamos al método 'iniciar' para que comience la ejecución.
    app.iniciar()
