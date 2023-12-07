"""Estudiante: Implementar la clase Estudiante con atributos como nombre,
edad y calificaciones. Utilizar el encapsulamiento para proteger los
datos que deban ser protegidos y proporcionar métodos públicos para
obtener dichos datos."""

class Estudiante:
    def __init__(self, nombre, edad, calificaciones):
        self.__nombre = nombre
        self.__edad = edad
        self.__calificaciones = calificaciones 

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_calificaciones(self):
        return self.__calificaciones

    def promedio_calificaciones(self):
        return sum(self.__calificaciones) / len(self.__calificaciones)


mi_estudiante = Estudiante('Leo', 20, [9, 10, 8, 9])

print(mi_estudiante.get_nombre())  
print(mi_estudiante.promedio_calificaciones()) 
