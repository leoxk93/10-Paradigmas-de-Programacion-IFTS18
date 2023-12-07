"""Animal: Utilizar la clase Animal del ejercicio de herencia y aplicar
polimorfismo para realizar el sonido característico del animal. Luego,
crear una lista de animales de diferentes tipos y utilizar el polimorfismo
para hacer que emiten sus sonidos."""

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "Guau Guau"

class Gato(Animal):
    def sonido(self):
        return "Miau Miau"

class Vaca(Animal):
    def sonido(self):
        return "Muu Muu"


animales = [Perro("Camila"), Gato("Bell"), Vaca("Cow")]

for animal in animales:
    print(f"El {animal.__class__.__name__} hace: {animal.sonido()}")
