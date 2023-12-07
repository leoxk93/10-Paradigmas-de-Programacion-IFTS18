"""Lee un archivo CSV que contiene registros de datos y convertirlo en un
archivo JSON."""

import csv
import json

def csv_a_json(archivo_csv, archivo_json):
    try:
        with open(archivo_csv, 'r') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)

            datos = [fila for fila in lector_csv]

        with open(archivo_json, 'w') as archivo_json:

            json.dump(datos, archivo_json, indent=2)

        print(f"Se ha convertido correctamente el archivo CSV '{archivo_csv}' a JSON en '{archivo_json}'.")

    except FileNotFoundError:
        print("Error: Archivo CSV no encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

archivo_csv = 'datos.csv'
archivo_json = 'datos.json'
csv_a_json(archivo_csv, archivo_json)
