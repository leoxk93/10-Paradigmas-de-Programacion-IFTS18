"""Hacer un administrador de contexto para notificar eventos al entrar y al
salir de un bloque de código."""

class Notificador:
    def __enter__(self):
        print("Entrando al bloque de código")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saliendo del bloque de código")
        if exc_type is not None:
            print(f"Ocurrió una excepción: {exc_val}")

with Notificador():
    print("Dentro del bloque de código")
