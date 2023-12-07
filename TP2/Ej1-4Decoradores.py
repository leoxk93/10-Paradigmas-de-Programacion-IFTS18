"""Hacer un decorador para verificar las precondiciones antes de ejecutar
una función."""

def verificar_precondiciones(*precondiciones):
    def decorador(funcion):
        def funcion_con_precondiciones(*args, **kwargs):
            for precondicion in precondiciones:
                assert precondicion(*args, **kwargs), "Precondición no satisfecha"
            return funcion(*args, **kwargs)
        return funcion_con_precondiciones
    return decorador

def es_positivo(x):
    return x > 0

@verificar_precondiciones(es_positivo)
def raiz_cuadrada(x):
    return x ** 0.5

print(raiz_cuadrada(9))  
print(raiz_cuadrada(-1))
