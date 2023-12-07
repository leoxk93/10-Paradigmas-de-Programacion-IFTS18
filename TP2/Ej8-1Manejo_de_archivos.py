"""Escribe un programa que abra un archivo de entrada, lea su contenido y
luego escriba ese contenido en un nuevo archivo de salida. Asegúrate
de cerrar ambos archivos al final."""

def copiar_contenido(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r') as f_entrada:
            contenido = f_entrada.read()

        with open(archivo_salida, 'w') as f_salida:
            f_salida.write(contenido)

        print(f"Se ha copiado el contenido de {archivo_entrada} a {archivo_salida}.")

    except FileNotFoundError:
        print("Error: Archivo de entrada no encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        if 'f_entrada' in locals() and not f_entrada.closed:
            f_entrada.close()
        if 'f_salida' in locals() and not f_salida.closed:
            f_salida.close()
 
archivo_entrada = 'archivo_entrada.txt'
archivo_salida = 'archivo_salida.txt'
copiar_contenido(archivo_entrada, archivo_salida)
