"""Hacer un decorador para agrega un retardo antes de que se ejecute
una función"""

import time

def retardo(segundos):
    def decorador(funcion):
        def funcion_con_retardo(*args, **kwargs):
            print(f"Esperando {segundos} segundos antes de ejecutar {funcion.__name__}")
            time.sleep(segundos)
            return funcion(*args, **kwargs)
        return funcion_con_retardo
    return decorador

@retardo(5)
def saludo():
    print("¡Hola, mundo!")

saludo()
