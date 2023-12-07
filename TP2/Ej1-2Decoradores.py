"""Hacer un decorador para verificar que los argumentos de una función
sean del tipo correcto."""

def check_types(*arg_types):
    def decorator(func):
        def wrapper(*args):
            if len(args) != len(arg_types):
                raise ValueError("Número incorrecto de argumentos")
            for arg, arg_type in zip(args, arg_types):
                if not isinstance(arg, arg_type):
                    raise TypeError(f"El argumento {arg} no es del tipo {arg_type}")
            return func(*args)
        return wrapper
    return decorator

@check_types(int, int)
def suma(a, b):
    return a + b

suma(1, 2)  
suma(1, "dos")  

"""Un asterisco delante de un parámetro en una función indica que ese único parámetro "recogerá" todos los parámetros posicionales
 que se le pasen a la función, y los hará disponibles en una tupla."""

"""Por otro lado el doble asterisco hace algo similar, pero con parámetros "con nombre". 
Al poner doble asterisco delante de un parámetro en una función, 
ese parámetro "recogerá" todos los parámetros con nombre que se le pasen en la invocación, 
y los hará disponibles para la función en un diccionario (las claves serían los nombres)."""