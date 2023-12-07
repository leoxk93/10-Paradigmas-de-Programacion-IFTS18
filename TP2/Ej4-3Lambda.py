"""Dada una lista de cadenas, utiliza map y una función lambda para crear
una lista con la longitud de cada palabra."""


lista = ['massa', 'bulrich', 'milei']

longitudes = list(map(lambda x: len(x), lista))

print(longitudes)
