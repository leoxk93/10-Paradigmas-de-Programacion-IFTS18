"""Imagina que estás desarrollando un sistema de gestión para una compañía de transporte. 
Tu objetivo es diseñar un conjunto de clases orientadas a objetos para manejar vehículos, rutas, conductores y clientes. 
Debes crear clases como 'Vehiculo', 'Ruta', 'Conductor' y 'Cliente'. 
Implementa herencia para representar diferentes tipos de vehículos, como 'Automovil' y 'Camion'. 
Utiliza la composición para gestionar la relación entre rutas, conductores y clientes, 
y asegúrate de que el diseño sea escalable para futuras funcionalidades del sistema de transporte."""

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self._marca = marca
        self._modelo = modelo
        self._año = año

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def año(self):
        return self._año

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self._tipo = tipo 

    @property
    def tipo(self):
        return self._tipo

class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self._capacidad_carga = capacidad_carga  # en toneladas

    @property
    def capacidad_carga(self):
        return self._capacidad_carga

class Ruta:
    def __init__(self, origen, destino):
        self._origen = origen
        self._destino = destino

    @property
    def origen(self):
        return self._origen

    @property
    def destino(self):
        return self._destino

class Persona:
    def __init__(self, nombre, apellido, dni):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def dni(self):
        return self._dni

class Conductor(Persona):
    def __init__(self, nombre, apellido, dni, licencia):
        super().__init__(nombre, apellido, dni)
        self._licencia = licencia

    @property
    def licencia(self):
        return self._licencia

class Cliente(Persona):
    def __init__(self, nombre, apellido, dni, email):
        super().__init__(nombre, apellido, dni)
        self._email = email

    @property
    def email(self):
        return self._email

class Viaje:
    def __init__(self, vehiculo, ruta, conductor, cliente):
        self._vehiculo = vehiculo
        self._ruta = ruta
        self._conductor = conductor
        self._cliente = cliente

    @property
    def vehiculo(self):
        return self._vehiculo

    @property
    def ruta(self):
        return self._ruta

    @property
    def conductor(self):
        return self._conductor

    @property
    def cliente(self):
        return self._cliente


"""Vehiculo es una clase base que define las propiedades comunes a todos los vehículos. 
Las clases Automovil y Camion heredan de Vehiculo y proporcionan propiedades adicionales específicas para cada tipo de vehículo.
La clase Ruta representa una ruta de transporte y tiene propiedades origen y destino.
Las clases Conductor y Cliente heredan de la clase Persona, lo que permite representar las propiedades comunes a todas las personas, como nombre, apellido y dni, y también propiedades específicas para conductores y clientes.
la clase Viaje representa un viaje y tiene propiedades vehiculo, ruta, conductor y cliente. 
Esta clase utiliza la composición para gestionar la relación entre vehículos, rutas, conductores y clientes. 
El uso de @property asegura que los atributos de las clases están correctamente encapsulados, proporcionando un buen nivel de abstracción. """