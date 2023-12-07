"""Libro: Crear las clases Libro y Libreria. La clase Libro debe incluir
atributos como titulo, autor y precio. La clase Libreria debe contener una
lista de objetos Libro y métodos para calcular el precio total de todos
los libros en la librería."""

from abc import ABC, abstractmethod

class Publicacion(ABC):
    @abstractmethod
    def obtener_informacion(self):
        pass

class Libro(Publicacion):
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def obtener_informacion(self):
        return f"Libro: {self.titulo} - Autor: {self.autor} - Precio: {self.precio}"

class Libreria:
    def __init__(self):
        self.publicaciones = []

    def agregar_publicacion(self, publicacion):
        if isinstance(publicacion, Publicacion):
            self.publicaciones.append(publicacion)
        else:
            raise TypeError("La publicación debe ser una instancia de la clase Publicacion")

    def calcular_precio_total(self):
        return sum([publicacion.precio for publicacion in self.publicaciones])


mi_libro = Libro("Don Quijote", "Miguel de Cervantes", 1000)
mi_libro_2 = Libro("Rodolfo Walsh", "Operacion Masacre", 2000)

mi_libreria = Libreria()  
mi_libreria.agregar_publicacion(mi_libro) 
mi_libreria.agregar_publicacion(mi_libro_2) 

for publicacion in mi_libreria.publicaciones:
    print(publicacion.obtener_informacion())

print(f"Precio total en la librería: {mi_libreria.calcular_precio_total()}")
