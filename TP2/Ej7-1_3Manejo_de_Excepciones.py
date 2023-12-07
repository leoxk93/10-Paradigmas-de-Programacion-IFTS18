"""Solicita al usuario que ingrese una cadena que represente un
número. Utiliza un bloque try y except para manejar la excepción
que se produce si la cadena no se puede convertir a un número."""

while True:
    numero = input("Por favor, ingresa un número: ")
    try:
        valor = float(numero)
        print(f"El número ingresado es {valor}.")
        break
    except ValueError:
        print("Eso no es un número válido. Por favor, intenta de nuevo.")
