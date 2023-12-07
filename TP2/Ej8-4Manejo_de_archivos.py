"""Escribe un programa que tome varios archivos de texto y los concatena
en un solo archivo de salida. Asegúrate de cerrar todos los archivos
correctamente."""

def concatenar_archivos(archivos_entrada, archivo_salida):
    try:
        with open(archivo_salida, 'w') as f_salida:
            for archivo_entrada in archivos_entrada:
                try:
                    with open(archivo_entrada, 'r') as f_entrada:
                        contenido = f_entrada.read()

                        f_salida.write(contenido)

                except FileNotFoundError:
                    print(f"Advertencia: Archivo {archivo_entrada} no encontrado. Se omitirá.")
                except Exception as e:
                    print(f"Ocurrió un error al procesar {archivo_entrada}: {e}")

        print(f"Se ha concatenado correctamente el contenido de los archivos en {archivo_salida}.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")


archivos_entrada = ['archivo1.txt', 'archivo2.txt', 'archivo3.txt']
archivo_salida = 'archivo_concatenado.txt'
concatenar_archivos(archivos_entrada, archivo_salida)
