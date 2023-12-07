"""Escribe una función recursiva para invertir una cadena."""

def invertir_cadena(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return invertir_cadena(cadena[1:]) + cadena[0]
