"""Crea un diccionario y luego intenta acceder a un valor utilizando
una clave que no está en el diccionario. Utiliza un bloque try y
except para manejar la excepción que se produce si la clave no
existe."""

mi_diccionario = {"clave1": "valor1", "clave2": "valor2"}

try:
    print(mi_diccionario["clave_no_existente"])
except KeyError:
    print("La clave no existe en el diccionario.")
