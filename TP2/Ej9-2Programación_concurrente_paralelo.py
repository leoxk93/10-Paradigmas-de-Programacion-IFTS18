"""Implementa el problema del productor-consumidor utilizando hilos,
donde un hilo produce datos y otro hilo los consume desde una cola
compartida."""

import threading
import queue
import time
import random

cola_compartida = queue.Queue(maxsize=5)  

def productor():
    for i in range(5): 
        dato = f'Dato-{i}'
        cola_compartida.put(dato)
        print(f"Productor produce: {dato}")
        time.sleep(random.uniform(0.1, 1))

def consumidor():
    for _ in range(5):  
        dato = cola_compartida.get()
        print(f"Consumidor consume: {dato}")
        time.sleep(random.uniform(0.1, 1))


hilo_productor = threading.Thread(target=productor)
hilo_consumidor = threading.Thread(target=consumidor)


hilo_productor.start()
hilo_consumidor.start()


hilo_productor.join()
hilo_consumidor.join()

print("Programa completado.")
