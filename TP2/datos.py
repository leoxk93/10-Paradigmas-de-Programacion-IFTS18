import csv

# Datos a escribir en el archivo CSV
datos = [
    ["Nombre", "Edad", "Ciudad"],
    ["Juan", 25, "Ciudad A"],
    ["María", 30, "Ciudad B"],
    ["Pedro", 28, "Ciudad A"],
]

archivo_csv = 'datos.csv'

try:
    with open(archivo_csv, 'w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)

        escritor_csv.writerows(datos)

    print(f"Se ha creado el archivo CSV '{archivo_csv}' correctamente.")

except Exception as e:
    print(f"Ocurrió un error: {e}")
