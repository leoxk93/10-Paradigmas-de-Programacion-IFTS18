""""Crea dos procesos utilizando la biblioteca multiprocessing y ejecuta
funciones diferentes en cada proceso."""

import multiprocessing
import time

def funcion_proceso1():
    for _ in range(5):
        print("Proceso 1 ejecutándose")
        time.sleep(1)

def funcion_proceso2():
    for _ in range(5):
        print("Proceso 2 ejecutándose")
        time.sleep(1)

if __name__ == "__main__":
    proceso1 = multiprocessing.Process(target=funcion_proceso1)
    proceso2 = multiprocessing.Process(target=funcion_proceso2)

    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()

    print("Ambos procesos han terminado.")
