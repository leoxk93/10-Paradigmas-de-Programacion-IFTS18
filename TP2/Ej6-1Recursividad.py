"""Escribe una función recursiva para encontrar y sumar todos los números
primos desde 1 hasta un número deseado."""

def es_primo(n, i=2):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % i == 0:
        return False
    elif i * i > n:
        return True
    else:
        return es_primo(n, i + 1)

def suma_primos(n):
    if n < 2:
        return 0
    elif es_primo(n):
        return n + suma_primos(n - 1)
    else:
        return suma_primos(n - 1)
