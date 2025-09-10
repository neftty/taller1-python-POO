# CLASE Calculadora

class Calculadora:
    def realizar_operacion(self, num1, num2, operacion):
        """
        Método que realiza un cálculo basado en la operación solicitada.
        """
        if operacion == "suma":
            return num1 + num2
        elif operacion == "resta":
            return num1 - num2
        elif operacion == "multiplicacion":
            return num1 * num2
        elif operacion == "division":
            
            if num2 == 0:
                return "Error: No se puede dividir por cero."
            else:
                return num1 / num2
        else:
            return "Error: Operación no válida."


class Aplicacion:
    def __init__(self):
        # Creamos un objeto de la clase Calculadora.
        self.calculadora = Calculadora()

    def iniciar(self):
        """
        Método que contiene el bucle principal de la calculadora.
        """
        print("¡Bienvenido a la Calculadora Simple!")

        while True:

            num1_str = input("\nIntroduce el primer número: ")
            num1 = float(num1_str)
            
            num2_str = input("Introduce el segundo número: ")
            num2 = float(num2_str)
            
            operacion = input("Elige la operación (suma, resta, multiplicacion, division): ").lower()

            resultado = self.calculadora.realizar_operacion(num1, num2, operacion)

            print("Resultado: " + str(resultado))

            continuar = input("\n¿Deseas realizar otro cálculo? (si/no): ").lower()
            if continuar != "si":
                break 
        
        print("\n¡Gracias por usar la calculadora! Adiós.")


#--------------------CÓDIGO PRINCIPAL----------------------

# 1. Creamos un objeto de la clase Aplicacion.
app = Aplicacion()

# 2. Llamamos al método 'iniciar' para que comience la ejecución.
app.iniciar()
