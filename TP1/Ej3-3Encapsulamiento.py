"""Coche: Crear la clase Coche con atributos privados y/o públicos según
corresponda de velocidad y kilometraje. Definir métodos públicos para
acelerar y registrar el kilometraje de manera segura."""

class Coche:
    def __init__(self):
        self.__velocidad = 0
        self.__kilometraje = 0

    def acelerar(self, incremento):
        self.__velocidad += incremento

    def registrar_kilometraje(self, kilometros):
        if kilometros >= 0:
            self.__kilometraje += kilometros
        else:
            print("El kilometraje no puede ser negativo.")

    def obtener_velocidad(self):
        return self.__velocidad

    def obtener_kilometraje(self):
        return self.__kilometraje


mi_coche = Coche()
mi_coche.acelerar(20)
mi_coche.registrar_kilometraje(100)
print(f"Velocidad: {mi_coche.obtener_velocidad()} km/h")
print(f"Kilometraje: {mi_coche.obtener_kilometraje()} km")
