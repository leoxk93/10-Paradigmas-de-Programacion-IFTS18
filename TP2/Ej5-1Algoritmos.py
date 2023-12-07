"""Escribe una función que sume los dígitos de un número pares de un
número entero. Si el número es impar, restarle 3 y sumarlo. Si el número
da negativo, sumar 1."""

def suma_digitos(n):
    digitos = [int(d) for d in str(n)]

    suma = 0
    
    for d in digitos:
        if d % 2 == 0:
            suma += d
        else:
            suma += (d - 3)
    
    if suma < 0:
        suma += 1
    
    return suma
