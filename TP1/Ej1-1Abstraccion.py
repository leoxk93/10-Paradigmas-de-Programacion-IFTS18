"""FiguraGeometrica: Utilizar clases FiguraGeometrica, Circulo, Rectangulo 
y Triangulo y que contenga métodos y atributos relacionados con el
cálculo del área y perímetro de una figura geométrica. Definan los
métodos y atributos necesarios para calcular el área y el perímetro de
cada tipo de figura utilizando los conceptos de abstracción."""


from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return math.pi * (self.radio**2)
    
    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura, lados):
        self.base = base
        self.altura = altura
        self.lados = lados
        
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        return sum(self.lados)


circulo = Circulo(8)
print(f"Área del círculo: {circulo.area()}")
print(f"Perímetro del círculo: {circulo.perimetro()}")

rectangulo = Rectangulo(8, 9)
print(f"Área del rectángulo: {rectangulo.area()}")
print(f"Perímetro del rectángulo: {rectangulo.perimetro()}")

triangulo = Triangulo(2, 4, (6, 8, 8))
print(f"Área del triángulo: {triangulo.area()}")
print(f"Perímetro del triángulo: {triangulo.perimetro()}")

