# =========================
# FUNCIONES DE EJERCICIOS
# =========================

def iniciar_sala(filas, columnas):
    return [[False for _ in range(columnas)] for _ in range(filas)]

def mostrar_sala(sala):
    print("\nMapa de la sala (O = libre, X = reservado):")
    for fila in sala:
        for asiento in fila:
            print("X" if asiento else "O", end=" ")
        print()

def reservar_asiento(sala, filas, columnas):
    while True:
        fila = int(input(f"Ingrese fila (0 a {filas-1}): "))
        col = int(input(f"Ingrese columna (0 a {columnas-1}): "))
        if fila < 0 or fila >= filas or col < 0 or col >= columnas:
            print("Posición inválida. Intenta de nuevo.")
        elif sala[fila][col]:
            print("Ese asiento ya está reservado.")
        else:
            sala[fila][col] = True
            print("Reserva realizada con éxito.")
            return 1

def ejecutar_reservas():
    filas, columnas = 5, 6
    sala = iniciar_sala(filas, columnas)
    disponibles = filas * columnas
    print("Bienvenido al sistema de reservas")
    while disponibles > 0:
        mostrar_sala(sala)
        print(f"Asientos disponibles: {disponibles}")
        opcion = input("¿Desea reservar un asiento? (si/no): ").strip().lower()
        if opcion == "si":
            disponibles -= reservar_asiento(sala, filas, columnas)
        else:
            break
    print("Fin del sistema de reservas.")

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def calcular(num1, num2, operacion):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        if num2 == 0:
            return "Error: División por cero"
        return num1 / num2
    else:
        return "Operación inválida"

def ejecutar_calculadora():
    while True:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        op = input("Operación (suma/resta/multiplicacion/division): ").lower()
        print("Resultado:", calcular(n1, n2, op))
        if input("¿Continuar? (si/no): ").lower() != "si":
            break

def controlar_invernadero():
    while True:
        temp = float(input("Ingrese la temperatura: "))
        if temp < 10:
            print("Encendiendo calefactor")
        elif 10 <= temp <= 25:
            print("Temperatura normal, sistema inactivo")
        else:
            print("Encendiendo ventilador")
        if input("¿Seguir controlando? (si/no): ").lower() != "si":
            break

def detectar_intrusos():
    noche = input("¿Es de noche? (si/no): ").lower() == "si"
    alarma = input("¿Desea activar la alarma? (si/no): ").lower() == "si"
    while alarma:
        sensores = []
        for i in range(3):
            valor = int(input(f"Sensor {i+1} (1=movimiento,0=no): "))
            sensores.append(valor)
        if sum(sensores) >= 2 and noche:
            print("¡ALERTA! Intruso detectado")
        else:
            print("Todo en calma")
        if input("¿Seguir monitoreando? (si/no): ").lower() != "si":
            break

def luces_domoticas():
    while True:
        noche = input("¿Es de noche? (si/no): ").lower() == "si"
        movimiento = input("¿Hay movimiento? (si/no): ").lower() == "si"
        if noche and movimiento:
            print("Luces ENCENDIDAS")
        else:
            print("Luces APAGADAS")
        if input("¿Seguir simulando? (si/no): ").lower() != "si":
            break

def aire_acondicionado():
    while True:
        temp = float(input("Ingrese la temperatura: "))
        humedad = float(input("Ingrese la humedad: "))
        if (temp > 28 and humedad > 60) or temp > 30:
            print("Aire acondicionado ENCENDIDO")
        else:
            print("Aire acondicionado APAGADO")
        if input("¿Seguir simulando? (si/no): ").lower() != "si":
            break

def control_acceso():
    while True:
        membresia = input("¿Tiene membresía? (si/no): ").lower() == "si"
        horario = input("¿Está en horario de atención? (si/no): ").lower() == "si"
        empleado = input("¿Es empleado? (si/no): ").lower() == "si"
        if (membresia and horario) or empleado:
            print("Acceso permitido")
        else:
            print("Acceso denegado")
        if input("¿Seguir controlando? (si/no): ").lower() != "si":
            break

def ingresar_datos():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    return nombre, apellido

def procesar_datos(nombre, apellido):
    return f"Hola {nombre} {apellido}, ¡bienvenido a nuestro sistema!"

def imprimir_saludo(mensaje):
    print(mensaje)

def ejecutar_saludo():
    nombre, apellido = ingresar_datos()
    mensaje = procesar_datos(nombre, apellido)
    imprimir_saludo(mensaje)


# =========================
# MENÚ PRINCIPAL
# =========================

def menu():
    while True:
        print("\n===============================")
        print("  Bienvenido al sistema de ejercicios en Python")
        print("===============================")
        print("Seleccione el ejercicio a resolver:")
        print("1. Sistema de Reservas")
        print("2. Juego FizzBuzz")
        print("3. Calculadora simple")
        print("4. Control de Temperatura (Invernadero)")
        print("5. Detección de Intrusos")
        print("6. Control de Luces Automático")
        print("7. Control de Aire Acondicionado")
        print("8. Control de Acceso a Tienda")
        print("9. Saludo personalizado")
        print("0. Salir")
        print("===============================")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            ejecutar_reservas()
        elif opcion == "2":
            fizzbuzz()
        elif opcion == "3":
            ejecutar_calculadora()
        elif opcion == "4":
            controlar_invernadero()
        elif opcion == "5":
            detectar_intrusos()
        elif opcion == "6":
            luces_domoticas()
        elif opcion == "7":
            aire_acondicionado()
        elif opcion == "8":
            control_acceso()
        elif opcion == "9":
            ejecutar_saludo()
        elif opcion == "0":
            print("¡Gracias por usar el sistema! Hasta pronto.")
            break
        else:
            print("Opción inválida, intente de nuevo.")

# Ejecutar el menú principal
menu()
