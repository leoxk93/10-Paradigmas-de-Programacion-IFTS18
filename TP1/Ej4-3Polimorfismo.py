"""Empleado: Utilizar la clase Empleado del ejercicio de herencia y aplicar
polimorfismo para calcular el salario de acuerdo con las reglas
específicas de cada tipo de empleado. Luego, crear una lista de
empleados de diferentes tipos y utilizar el polimorfismo para calcular
sus salarios."""

class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

class Gerente(Empleado):
    def calcular_salario(self):
        return self.salario_base * 1.10

class Ingeniero(Empleado):
    def calcular_salario(self):
        return self.salario_base * 1.20

empleados = [Gerente("Leo", 3000), Ingeniero("Julieta", 3000)]

for empleado in empleados:
    print(f"El salario de {empleado.nombre} es: {empleado.calcular_salario()}")
