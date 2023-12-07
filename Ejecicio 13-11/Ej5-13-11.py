"""Supongamos que estás trabajando en un sistema de gestión de un gimnasio. 
Tu tarea es diseñar un conjunto de clases orientadas a objetos para administrar socios, entrenadores, clases y pagos. 
Debes crear clases como 'Socio', 'Entrenador', 'Clase' y 'Pago'. Aplica herencia para representar diferentes niveles de socios, 
como 'SocioRegular' y 'SocioPremium'. Utiliza la composición para manejar la relación entre socios, clases y pagos,
y asegúrate de que el diseño sea versátil para futuras funcionalidades del gimnasio."""

from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, apellido, dni):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni

    @abstractmethod
    def mostrar_info(self):
        pass

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def dni(self):
        return self._dni

class Socio(Persona):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)
        self._clases = []
        self._pagos = []

    def mostrar_info(self):
        return f"Socio: {self.nombre} {self.apellido}, DNI: {self.dni}"

    @property
    def clases(self):
        return self._clases

    @property
    def pagos(self):
        return self._pagos

class SocioRegular(Socio):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)

class SocioPremium(Socio):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)

class Entrenador(Persona):
    def __init__(self, nombre, apellido, dni, especialidad):
        super().__init__(nombre, apellido, dni)
        self._especialidad = especialidad

    def mostrar_info(self):
        return f"Entrenador: {self.nombre} {self.apellido}, DNI: {self.dni}, Especialidad: {self.especialidad}"

    @property
    def especialidad(self):
        return self._especialidad

class Clase:
    def __init__(self, nombre, entrenador):
        self._nombre = nombre
        self._entrenador = entrenador

    @property
    def nombre(self):
        return self._nombre

    @property
    def entrenador(self):
        return self._entrenador

class Pago:
    def __init__(self, socio, monto, fecha):
        self._socio = socio
        self._monto = monto
        self._fecha = fecha

    @property
    def socio(self):
        return self._socio

    @property
    def monto(self):
        return self._monto

    @property
    def fecha(self):
        return self._fecha

"""En este diseño, Persona es una clase abstracta que define la interfaz para todas las personas 
con un método mostrar_info y propiedades nombre, apellido y dni. 
Las clases Socio y Entrenador heredan de Persona y proporcionan implementaciones concretas del método mostrar_info.
Las clases SocioRegular y SocioPremium heredan de Socio, lo que permite representar diferentes niveles de socios.
La clase Clase representa una clase de gimnasio y tiene propiedades nombre y entrenador.
La clase Pago representa un pago y tiene propiedades socio, monto y fecha.
El uso de @property asegura que los atributos de las clases están correctamente encapsulados, proporcionando un buen nivel de abstracción."""
