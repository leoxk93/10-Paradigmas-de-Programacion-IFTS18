"""Forma: Implementar las clases Forma, Circulo y Rectangulo. La o las
clases deben contener atributos como color y dimensiones. Las
subclases deben heredar y definir métodos y atributos para calcular el
área y el perímetro de cada forma."""

import math

class Forma:
    def __init__(self, color):
        self.color = color

class Circulo(Forma):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(Forma):
    def __init__(self, color, ancho, alto):
        super().__init__(color)
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)



mi_circulo = Circulo('rojo', 10)
mi_rectangulo = Rectangulo('azul', 5, 10)

print(mi_circulo.color)  
print(mi_circulo.area()) 
print(mi_rectangulo.perimetro()) 
