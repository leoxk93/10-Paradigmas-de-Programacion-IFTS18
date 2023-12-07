"""Imagina que estás trabajando en un programa de gestión de un sistema educativo. 
Tu tarea es diseñar un conjunto de clases orientadas a objetos para administrar estudiantes, profesores, asignaturas y calificaciones. 
Debes crear clases como 'Estudiante', 'Profesor', 'Asignatura' y 'Calificacion'. 
Implementa herencia para representar diferentes niveles de estudiantes, como 'EstudianteRegular' y 'EstudianteAvanzado'. 
Utiliza la composición para gestionar la relación entre estudiantes, asignaturas y calificaciones, 
y asegúrate de que el diseño sea versátil para futuras funcionalidades del sistema educativo."""

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

class Estudiante(Persona):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)
        self._asignaturas = []
        self._calificaciones = []

    def mostrar_info(self):
        return f"Estudiante: {self.nombre} {self.apellido}, DNI: {self.dni}"

    @property
    def asignaturas(self):
        return self._asignaturas

    @property
    def calificaciones(self):
        return self._calificaciones

class EstudianteRegular(Estudiante):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)

class EstudianteAvanzado(Estudiante):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)

class Profesor(Persona):
    def __init__(self, nombre, apellido, dni, asignatura):
        super().__init__(nombre, apellido, dni)
        self._asignatura = asignatura

    def mostrar_info(self):
        return f"Profesor: {self.nombre} {self.apellido}, DNI: {self.dni}, Asignatura: {self.asignatura.nombre}"

    @property
    def asignatura(self):
        return self._asignatura

class Asignatura:
    def __init__(self, nombre, codigo):
        self._nombre = nombre
        self._codigo = codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def codigo(self):
        return self._codigo

class Calificacion:
    def __init__(self, estudiante, asignatura, nota):
        self._estudiante = estudiante
        self._asignatura = asignatura
        self._nota = nota

    @property
    def estudiante(self):
        return self._estudiante

    @property
    def asignatura(self):
        return self._asignatura

    @property
    def nota(self):
        return self._nota


"""Persona es una clase abstracta que define la interfaz para todas las personas con un método mostrar_info y propiedades nombre, apellido y dni. 
Las clases Estudiante y Profesor heredan de Persona.
Las clases EstudianteRegular y EstudianteAvanzado heredan de Estudiante, lo que permite representar diferentes niveles de estudiantes.
La clase Asignatura representa una asignatura y tiene propiedades nombre y codigo.
La clase Calificacion representa una calificación y tiene propiedades estudiante, asignatura y nota."""