"""Diseña un sistema de gestión de personal para una empresa. Debes
implementar las siguientes clases:
Persona: Una clase base que representa a una persona con atributos como
nombre, edad y DNI. Utiliza el encapsulamiento para proteger los datos
sensibles.

Empleado: Una subclase de Persona que agrega atributos como salario y
cargo. Implementa el cálculo del salario en base al cargo y permite consultar el
salario.

Gerente: Una subclase de Empleado que agrega atributos específicos de un
gerente, como departamento.

Departamento: Una clase que contiene una lista de empleados y métodos
para agregar, eliminar y consultar empleados.

Crea instancias de estas clases y demuestra cómo agregar empleados a un
departamento, calcular salarios y acceder a la información de las personas
Importante"""

class Persona:
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni


class Empleado(Persona):
    def __init__(self, nombre, edad, dni, salario, cargo):
        super().__init__(nombre, edad, dni)
        self.__salario = salario
        self.__cargo = cargo

    @property
    def salario(self):
        return self.__salario

    @property
    def cargo(self):
        return self.__cargo


class Gerente(Empleado):
    def __init__(self, nombre, edad, dni, salario, cargo, departamento):
        super().__init__(nombre, edad, dni, salario, cargo)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento


class Departamento:
    def __init__(self):
        self.__empleados = []

    def agregar_empleado(self, empleado):
        self.__empleados.append(empleado)

    def eliminar_empleado(self, empleado):
        self.__empleados.remove(empleado)

    def consultar_empleados(self):
        for empleado in self.__empleados:
            print(f'Nombre: {empleado.nombre}, Edad: {empleado.edad}, DNI: {empleado.dni}, Salario: {empleado.salario}, Cargo: {empleado.cargo}')






"""Para resolver este ejercicio, apliqué varios conceptos de la Programación Orientada a Objetos (POO):

Herencia: La herencia es un principio de la POO que permite crear nuevas clases a partir de clases existentes. En este caso, Empleado es una subclase de Persona y Gerente es una subclase de Empleado. Esto significa que Empleado hereda los atributos y métodos de Persona y Gerente hereda los atributos y métodos de Empleado.

Encapsulamiento: El encapsulamiento es otro principio de la POO que se utiliza para ocultar los detalles internos de una clase y proteger los datos. En este caso, todos los atributos de las clases Persona, Empleado, Gerente y Departamento están encapsulados utilizando métodos getter (a través del decorador @property).

Composición: La composición es un principio de la POO que permite construir clases complejas a partir de clases más simples. En este caso, la clase Departamento está compuesta por objetos de la clase Empleado."""