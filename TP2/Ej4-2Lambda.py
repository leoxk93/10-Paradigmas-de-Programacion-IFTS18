"""Toma una lista de cadenas y utiliza map con una función lambda para
convertir todas las cadenas en mayúsculas."""


lista = ['massa', 'bulrich', 'milei']


lista_mayusculas = list(map(lambda x: x.upper(), lista))

print(lista_mayusculas)
