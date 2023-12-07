"""Escribe un programa que solicite al usuario dos números y realice
la división de uno por el otro. Utiliza un bloque try y except para
manejar la excepción que ocurre si el segundo número es cero."""

try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    resultado = num1 / num2
    print("El resultado de la división es: ", resultado)

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
    
except ValueError:
    print("Error: Debes introducir un número.")
