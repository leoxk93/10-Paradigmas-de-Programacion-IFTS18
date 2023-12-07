"""Empleado: Crear las clases Empleado, Gerente y Trabajador. Se debe
tener atributos como nombre, salario y departamento. Las subclases
deben heredar y definir los métodos y atributos necesarios para
representar cada tipo de empleado."""

class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, num_empleados):
        super().__init__(nombre, salario, departamento)
        self.num_empleados = num_empleados

class Trabajador(Empleado):
    def __init__(self, nombre, salario, departamento, horas_trabajadas):
        super().__init__(nombre, salario, departamento)
        self.horas_trabajadas = horas_trabajadas


mi_gerente = Gerente('Carl', 300000, 'Ventas', 10)
mi_trabajador = Trabajador('Lenny', 200000, 'Producción', 40)

print(mi_gerente.nombre)  
print(mi_trabajador.horas_trabajadas)
