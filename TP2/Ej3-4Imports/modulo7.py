"""Crear dos módulos en el mismo directorio. Desde un módulo, importa
una función o variable del otro utilizando una importación absoluta y
generar un error de importación circular."""

from modulo8 import despedida

def saludo():
    return "¡Hola desde el módulo 7!"
