"""Utiliza un pool de procesos para realizar operaciones en paralelo en
una lista de datos."""

import multiprocessing

def operacion(elemento):
    return elemento * 2

if __name__ == "__main__":
    datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    numero_procesos = 4

    with multiprocessing.Pool(processes=numero_procesos) as pool:
        resultados = pool.map(operacion, datos)


    print("Lista original:", datos)
    print("Resultados después de la operación en paralelo:", resultados)
