"""Dada una lista de números, utiliza map y una función lambda para crear
una nueva lista que contenga el doble de cada número."""

numeros = [4, 8, 15, 16, 23, 42]

dobles = list(map(lambda x: x * 10, numeros))

print(dobles)


