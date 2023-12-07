"""Crea dos hilos que ejecuten dos funciones diferentes simultáneamente
y muestran mensajes de salida."""

import threading
import time

def funcion1():
    for _ in range(5):
        print("Función 1 ejecutándose")
        time.sleep(1)

def funcion2():
    for _ in range(5):
        print("Función 2 ejecutándose")
        time.sleep(1)

hilo1 = threading.Thread(target=funcion1)
hilo2 = threading.Thread(target=funcion2)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print("Ambos hilos han terminado.")
