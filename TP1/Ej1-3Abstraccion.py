"""Vehiculo: Implementar las clases Vehiculo, Coche, Motocicleta y
Bicicleta. La clase Vehiculo debe tener propiedades como marca,
modelo y velocidad_maxima. Cada subclase debe definir sus métodos y
atributos específicos relacionados con el comportamiento de cada tipo
de vehículo."""


class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, num_puertas):
        super().__init__(marca, modelo, velocidad_maxima)
        self.num_puertas = num_puertas

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, tipo):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo = tipo  

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, tipo):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo = tipo  


mi_coche = Coche('Renault', 'Sandero', 170, 4)
mi_moto = Motocicleta('Yamaha', 'YZF-R1', 299, 'Deportiva')
mi_bici = Bicicleta('Trek', 'Domane SLR', 60, 'Montaña')


print(mi_coche.marca)  # Imprime: Renault
print(mi_moto.tipo)    # Imprime: Deportiva
print(mi_bici.velocidad_maxima)  # Imprime: 60
