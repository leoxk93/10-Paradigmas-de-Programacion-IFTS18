"""Escribe un programa que intente abrir un archivo que no existe y
utilice un bloque try y except para manejar la excepción de
"FileNotFoundError"."""

try:
    with open('archivo_no_existente.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo no se encontró.")
