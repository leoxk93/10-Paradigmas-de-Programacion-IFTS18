"""Lee un archivo CSV que contiene registros de datos y realiza alguna
operación de procesamiento en los datos, cómo calcular promedios,
encontrar valores máximos o mínimos, o filtrar registros que cumplan
ciertas condiciones."""

import csv

def procesar_csv(archivo_csv, columna_para_promedio):
    try:
        with open(archivo_csv, 'r') as archivo:
            # Crea un objeto lector CSV
            lector_csv = csv.reader(archivo)

            encabezados = next(lector_csv)

            indice_columna = encabezados.index(columna_para_promedio)

            suma = 0
            cantidad_filas = 0

            for fila in lector_csv:
                valor_columna = float(fila[indice_columna])

                suma += valor_columna
                cantidad_filas += 1

            if cantidad_filas > 0:
                promedio = suma / cantidad_filas
                print(f"El promedio de la columna '{columna_para_promedio}' es: {promedio}")
            else:
                print("No hay datos para calcular el promedio.")

    except FileNotFoundError:
        print("Error: Archivo CSV no encontrado.")
    except ValueError:
        print("Error: No se pudo convertir un valor a número.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

archivo_csv = 'datos.csv'
columna_para_promedio = 'columna_de_interes'
procesar_csv(archivo_csv, columna_para_promedio)
