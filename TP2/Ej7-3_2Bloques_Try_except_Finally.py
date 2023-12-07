"""Crea un programa que solicite al usuario dos números y una
operación matemática (suma, resta, multiplicación, división) para
realizar. Utiliza bloques try, except y finally para manejar cualquier
excepción que pueda ocurrir durante la operación y asegurarte
de que los recursos se liberen correctamente."""


try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    operacion = input("Introduce una operación matemática (suma, resta, multiplicación, división): ")

    if operacion == "suma":
        resultado = num1 + num2
    elif operacion == "resta":
        resultado = num1 - num2
    elif operacion == "multiplicación":
        resultado = num1 * num2
    elif operacion == "división":
        resultado = num1 / num2
    else:
        print("Operación no reconocida.")

    print(f"El resultado es: {resultado}")

except ZeroDivisionError:
    print("Error: División por cero.")
except ValueError:
    print("Error: Entrada no válida. Por favor, introduce un número.")
except Exception as e:
    print(f"Error: {e}")

finally:
    print("Fin del programa.")
