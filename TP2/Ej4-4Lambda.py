"""Toma una lista de números y utiliza map con una función lambda para
calcular la raíz cuadrada de cada número."""

import math

lista = [4, 8, 15, 16, 23, 42]

raices = list(map(lambda x: math.sqrt(x), lista))

print(raices)
