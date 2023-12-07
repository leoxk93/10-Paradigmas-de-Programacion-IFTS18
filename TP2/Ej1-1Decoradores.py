"""Hacer un decorador para registrar las llamadas a una función, junto con
sus argumentos y resultados."""

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__} con argumentos {args} y {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} devolvió {result}")
        return result
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

@log_calls
def suma(a, b):
    return a + b

suma(1, 2)

"""El principal uso de *args y **kwargs es en la definición de funciones. 
Ambos permiten pasar un número variable de argumentos a una función, por lo que si quieres definir una función cuyo número de parámetros de entrada puede ser variable, considera el uso de *args o **kwargs como una opción. De hecho, el nombre de args viene de argumentos, 
que es como se denominan en programación a los parámetros de entrada de una función."""

"""**kwargs permite pasar argumentos de longitud variable asociados con un nombre o key a una función. 
Deberías usar **kwargs si quieres manejar argumentos con nombre como entrada a una función."""""