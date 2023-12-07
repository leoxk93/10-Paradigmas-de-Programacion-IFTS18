"""Diseñar clases utilizando Programación Orientada a Objetos y Composición
1.1. Imagina que estás desarrollando un emocionante videojuego de carreras de autos.
Tu tarea es diseñar un sistema de clases orientadas a objetos para gestionar los
autos, los pilotos y las pistas de carreras. Debes crear clases para representar un
'Auto', 'Piloto', 'Pista' y al menos una clase adicional que herede de 'Auto' para
representar diferentes tipos de vehículos (por ejemplo, coches deportivos, camiones,
etc.). Utiliza la composición y asegúrate de que el diseño sea flexible y expansible
para futuras características del juego. Describe las propiedades y métodos
esenciales de cada clase y cómo se relacionan entre sí en el contexto del juego de
carreras de autos. Aplicar al menos un ejemplo de cada pilar de la POO.

2. Programación orientada a objetos
2.1. ¿Cuáles son los pilares? Explicar cada uno de ellos?
2.2. ¿Cuál es la diferencia entre una clase y un objeto en POO?
2.3. ¿Qué son los métodos de acceso y los métodos de modificación?
2.4. ¿Cuál es el propósito de los métodos de modificación?
2.5. Explica la diferencia entre una variable de clase y una variable de instancia.
2.6. ¿Qué es la encapsulación y cómo se implementa? ¿Por qué es importante?

3. Diseño de clases
3.1. ¿Qué es la relación “Es un”? Explicar y dar ejemplo en código
3.2. ¿Qué es la relación “Tiene un”? Explicar y dar ejemplos en código

4. Buenas prácticas
4.1. ¿Qué son las buenas prácticas de programación? ¿Por qué es importante seguir un
estándar?
4.2. ¿Por qué es fundamental evitar la duplicación de código? ¿Cómo logramos esto?

5. Algoritmos
5.1. ¿Qué es la recursividad? Explicar y dar ejemplos de uso
5.2. ¿Qué son los administradores de contexto? ¿Cuáles son sus principales usos?
5.3. ¿Qué son los decoradores? ¿Podemos crear nuestros propios decoradores?
5.4. ¿Cuándo utilizarías administrador de contexto en lugar de un decorador?
5.5. ¿Qué tipos de imports existen?
"""
from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    @abstractmethod
    def acelerar(self, cantidad):
        pass

    @property
    def velocidad(self):
        return self.velocidad_actual

class Deportivo(Auto):
    def acelerar(self, cantidad):
        self.velocidad_actual += cantidad
        if self.velocidad_actual > self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima

class Camion(Auto):
    def acelerar(self, cantidad):
        self.velocidad_actual += cantidad // 2
        if self.velocidad_actual > self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima

class Piloto:
    def __init__(self, nombre, auto):
        self.nombre = nombre
        self.auto = auto

    def acelerar_auto(self, cantidad):
        self.auto.acelerar(cantidad)

class Pista:
    def __init__(self, longitud):
        self.longitud = longitud

    def correr_carrera(self, pilotos):
        for piloto in pilotos:
            while piloto.auto.velocidad < self.longitud:
                piloto.acelerar_auto(10)
        print("¡La carrera ha terminado!")


"""En este diseño, Auto es una clase abstracta que define la interfaz para todos los autos con un método acelerar y una propiedad velocidad. 
Las clases Deportivo y Camion heredan de Auto y proporcionan implementaciones concretas del método acelerar.
La clase Piloto utiliza la composición para tener un Auto. 
Esto significa que un Piloto tiene un Auto, pero no es un Auto, lo que es un ejemplo de la relación “tiene-un”.
Finalmente, la clase Pista representa la pista de carreras y tiene un método correr_carrera que acepta una lista de Pilotos y simula una carrera.
Este diseño es flexible y expansible. 
Por ejemplo, se pueden agregar más tipos de autos simplemente creando más clases que hereden de Auto. 
También se pueden agregar más comportamientos a los Pilotos o a la Pista según sea necesario para las características futuras del juego."""

