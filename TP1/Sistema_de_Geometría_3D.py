"""Sistema de Geometría 3D
Diseña un sistema de geometría tridimensional que trabaje con figuras en el
espacio 3D. Debes implementar las siguientes clases:

Punto3D: Una clase que representa un punto en el espacio 3D con
coordenadas x, y, y z.

Figura3D: Una clase abstracta que representa una figura tridimensional y
define métodos abstractos para calcular su volumen y área superficial.

Cubo, Esfera y Cilindro: Subclases de Figura3D que implementan los métodos
para calcular el volumen y área superficial específicos de cada figura.

Crea instancias de estas clases y demuestra cómo calcular el volumen y área
superficial de diferentes figuras tridimensionales."""

from abc import ABC, abstractmethod
import math

class Punto3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Figura3D(ABC):
    @abstractmethod
    def volumen(self):
        pass

    @abstractmethod
    def area_superficial(self):
        pass

class Cubo(Figura3D):
    def __init__(self, longitud_lado):
        self.longitud_lado = longitud_lado

    def volumen(self):
        return self.longitud_lado ** 3

    def area_superficial(self):
        return 6 * (self.longitud_lado ** 2)

class Esfera(Figura3D):
    def __init__(self, radio):
        self.radio = radio

    def volumen(self):
        return (4/3) * math.pi * (self.radio ** 3)

    def area_superficial(self):
        return 4 * math.pi * (self.radio ** 2)

class Cilindro(Figura3D):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def volumen(self):
        return math.pi * (self.radio ** 2) * self.altura

    def area_superficial(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)


cubo = Cubo(3)
esfera = Esfera(2)
cilindro = Cilindro(2, 5)

for figura in [cubo, esfera, cilindro]:
    print(f"Volumen de {figura.__class__.__name__}: {figura.volumen()}")
    print(f"Área superficial de {figura.__class__.__name__}: {figura.area_superficial()}")



"""Este diseño utiliza los conceptos de la Programación Orientada a Objetos (POO) 
Encapsulación: Los detalles de implementación de las clases están ocultos y solo se exponen los métodos necesarios. 
Herencia: Las clases Cubo, Esfera y Cilindro heredan de la clase abstracta Figura3D.
Polimorfismo: El código que calcula el volumen y área superficial es capaz de trabajar con objetos de cualquier clase que herede de Figura3D.
Abstraccion: Figura 3D es un clase abstracta que hereda a multiples figuras diferentes"""