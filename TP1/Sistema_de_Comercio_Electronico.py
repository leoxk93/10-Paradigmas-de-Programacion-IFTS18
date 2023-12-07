"""Diseña un sistema de comercio electrónico para una tienda en línea. Debes
implementar las siguientes clases:
Producto: Una clase que representa un producto con atributos como nombre,
precio, cantidad en stock, etc.
CarritoCompra: Una clase que representa el carrito de compras de un cliente.
Debe permitir agregar, eliminar y calcular el total de los productos en el carrito.
Cliente: Una clase que representa a un cliente con atributos como nombre,
dirección, carrito de compra, etc.
Crea instancias de estas clases y demuestra cómo un cliente puede agregar
productos a su carrito, realizar una compra y calcular el total.
Importante."""

from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio, cantidad_en_stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad_en_stock = cantidad_en_stock

    @abstractmethod
    def obtener_nombre(self):
        pass

    @abstractmethod
    def obtener_precio(self):
        pass

    @abstractmethod
    def obtener_cantidad_en_stock(self):
        pass

    @abstractmethod
    def actualizar_stock(self, cantidad):
        pass


class CarritoCompra(ABC):
    def __init__(self):
        self.__productos = []

    @abstractmethod
    def agregar_producto(self, producto):
        pass

    @abstractmethod
    def eliminar_producto(self, producto):
        pass

    @abstractmethod
    def calcular_total(self):
        pass

    @abstractmethod
    def obtener_productos(self):
        pass


class Cliente:
    def __init__(self, nombre, direccion):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__carrito = CarritoCompra()

    def agregar_producto_al_carrito(self, producto):
        self.__carrito.agregar_producto(producto)

    def eliminar_producto_del_carrito(self, producto):
        self.__carrito.eliminar_producto(producto)

    def realizar_compra(self):
        total = self.__carrito.calcular_total()
        for producto in self.__carrito.obtener_productos():
            cantidad_comprada = 1  
            producto.actualizar_stock(cantidad_comprada)
        self.__carrito = CarritoCompra()  
        return total


class ProductoConcreto(Producto):
    def obtener_nombre(self):
        return self._Producto__nombre

    def obtener_precio(self):
        return self._Producto__precio

    def obtener_cantidad_en_stock(self):
        return self._Producto__cantidad_en_stock

    def actualizar_stock(self, cantidad):
        self._Producto__cantidad_en_stock -= cantidad


class CarritoCompraConcreto(CarritoCompra):
    def __init__(self):
        super().__init__()

    def agregar_producto(self, producto):
        self._CarritoCompra__productos.append(producto)

    def eliminar_producto(self, producto):
        self._CarritoCompra__productos.remove(producto)

    def calcular_total(self):
        return sum([producto.obtener_precio() for producto in self._CarritoCompra__productos])

    def obtener_productos(self):
        return self._CarritoCompra__productos



manzana = ProductoConcreto("Manzana", 0.5, 10)
pera = ProductoConcreto("Pera", 0.6, 8)

cliente = Cliente("Homero", "Calle Falsa 123")
carrito = CarritoCompraConcreto()

cliente.agregar_producto_al_carrito(manzana)
cliente.agregar_producto_al_carrito(pera)

total = cliente.realizar_compra()
print(f"El total de la compra es: {total}")



"""Este diseño utiliza los conceptos de la Programación Orientada a Objetos (POO) 
Encapsulación: Los detalles de implementación de las clases están ocultos y solo se exponen los métodos necesarios. 
Polimorfismo: El método agregar_producto del carrito de compras puede trabajar con cualquier objeto que sea una instancia de la clase Producto."""

