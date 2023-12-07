"""Crea una lista de números y, a continuación, intenta acceder a un
elemento en un índice especificado por el usuario. Utiliza un
bloque try y except para manejar la excepción que se produce si
el índice está fuera de rango."""

numeros = [1, 2, 3, 4, 5]

try:
    indice = int(input("Introduce un índice: "))
    print("El número en el índice especificado es: ", numeros[indice])

except IndexError:
    print("Error: El índice está fuera de rango.")
    
except ValueError:
    print("Error: Debes introducir un número entero.")
