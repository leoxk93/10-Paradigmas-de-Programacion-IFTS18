"""Capturar las excepciones personalizadas en el punto 7.2, imprimir
un mensaje en pantalla y lanzarlas nuevamente."""

# Excepción personalizada para la división (7.1.1)
class DivisionError(Exception):
    pass

try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    
    if num2 == 0:
        raise DivisionError("Error: No se puede dividir por cero.")
    
    resultado = num1 / num2
    print("El resultado de la división es: ", resultado)

except DivisionError as e:
    print(f"Capturada la excepción personalizada: {e}")
    raise e

except ValueError:
    print("Error: Debes introducir un número.")


# Excepción personalizada para el acceso a la lista (7.1.2)
class ListIndexError(Exception):
    pass

numeros = [1, 2, 3, 4, 5]

try:
    indice = int(input("Introduce un índice: "))
    
    if indice < 0 or indice >= len(numeros):
        raise ListIndexError("Error: El índice está fuera de rango.")
    
    print("El número en el índice especificado es: ", numeros[indice])

except ListIndexError as e:
    print(f"Capturada la excepción personalizada: {e}")
    raise e

except ValueError:
    print("Error: Debes introducir un número entero.")


# Excepción personalizada para la conversión a número (7.1.3)
class InvalidNumberError(Exception):
    pass

while True:
    numero = input("Por favor, ingresa un número: ")
    
    try:
        valor = float(numero)
        print(f"El número ingresado es {valor}.")
        break
    except InvalidNumberError as e:
        print(f"Capturada la excepción personalizada: {e}")
        raise e
    except ValueError:
        raise InvalidNumberError("Eso no es un número válido. Por favor, intenta de nuevo.") from None


# Excepción personalizada para el archivo no encontrado (7.1.4)
class FileNotFoundErrorCustom(Exception):
    pass

try:
    with open('archivo_no_existente.txt', 'r') as f:
        print(f.read())
except FileNotFoundErrorCustom as e:
    print(f"Capturada la excepción personalizada: {e}")
    raise e


# Excepción personalizada para la clave no encontrada en el diccionario (7.1.5)
class KeyNotFoundError(Exception):
    pass

mi_diccionario = {"clave1": "valor1", "clave2": "valor2"}

try:
    print(mi_diccionario["clave_no_existente"])
except KeyNotFoundError as e:
    print(f"Capturada la excepción personalizada: {e}")
    raise e
except KeyError:
    raise KeyNotFoundError("La clave no existe en el diccionario.") from None
