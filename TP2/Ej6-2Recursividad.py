"""Escribe una función recursiva para calcular el MCD (Maximo Comun Divisor) de dos números
enteros."""

def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)
