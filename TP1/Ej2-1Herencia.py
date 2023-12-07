"""Animal: Utilizar las clases Animal, Perro, Gato y Pájaro. Se debe incluir
atributos como nombre y edad. Las subclases deben heredar y definir
métodos y atributos relacionados con el comportamiento y
características de cada tipo de animal."""

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def sonido(self):
        pass
    
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

class Perro(Animal):
    def sonido(self):
        return "Guau"

class Gato(Animal):
    def sonido(self):
        return "Miau"

class Pajaro(Animal):
    def __init__(self, nombre, edad, tipo_plumaje):
        super().__init__(nombre, edad)
        self.tipo_plumaje = tipo_plumaje
    
    def sonido(self):
        return "Pío pío"
    
    def volar(self):
        return f"{self.nombre} está volando con sus alas de plumaje {self.tipo_plumaje}"


perro = Perro("Max", 5)
gato = Gato("Mefisto", 3)
pajaro = Pajaro("Loco", 2, "colorido")

print(perro)
print(f"Sonido: {perro.sonido()}")

print(gato)
print(f"Sonido: {gato.sonido()}")

print(pajaro)
print(f"Sonido: {pajaro.sonido()}")
print(pajaro.volar())
