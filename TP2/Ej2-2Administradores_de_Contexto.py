"""Crea un administrador de contexto que permita cambiar el directorio de
trabajo al entrar en un bloque y volver al directorio original al salir."""

import os

class CambiarDirectorio:
    def __init__(self, nuevo_directorio):
        self.nuevo_directorio = nuevo_directorio
        self.directorio_original = None

    def __enter__(self):
        self.directorio_original = os.getcwd()
        os.chdir(self.nuevo_directorio)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.directorio_original)

with CambiarDirectorio('/ruta/al/nuevo/directorio'):
    pass
