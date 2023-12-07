""""FiguraGeometrica: Utilizar la clase FiguraGeometrica del ejercicio de
abstracción y crear un método muestre información específica de la
figura utilizando polimorfismo. Luego, crear una lista de figuras
geométricas de diferentes tipos y utilizar el polimorfismo para imprimir
su información."""


import math


class FiguraGeometrica:
    def area(self):
        pass
    
    def perimetro(self):
        pass
    
    def informacion(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return math.pi * self.radio**2
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def informacion(self):
        return f"Círculo - Radio: {self.radio}"

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    def informacion(self):
        return f"Rectángulo - Base: {self.base}, Altura: {self.altura}"

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def informacion(self):
        return f"Triángulo - Base: {self.base}, Altura: {self.altura}, Lados: {self.lado1}, {self.lado2}, {self.lado3}"


figuras = [Circulo(5), Rectangulo(4, 6), Triangulo(3, 4, 5, 5, 4)]


for figura in figuras:
    print(figura.informacion())
