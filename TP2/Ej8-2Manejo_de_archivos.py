"""Escribe un programa que abra un archivo de texto, cuente cuántas
palabras contiene y muestre el resultado en la pantalla."""

def contar_palabras(archivo):
    try:
        # Modo lectura
        with open(archivo, 'r') as f:

            contenido = f.read()

            palabras = contenido.split()

            cantidad_palabras = len(palabras)

            print(f"El archivo {archivo} contiene {cantidad_palabras} palabras.")

    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:

        if 'f' in locals() and not f.closed:
            f.close()


archivo_a_contar = 'archivo_entrada.txt'
contar_palabras(archivo_a_contar)
