"""Escribe un programa que abra un archivo, lea su contenido y
escriba el mismo contenido en otro archivo. Utiliza bloques try,
except y finally para manejar cualquier excepción que pueda
ocurrir durante la lectura o escritura, y asegúrate de que ambos
archivos se cierren correctamente."""

try:
    archivo_origen = open('nombre_del_archivo_origen.txt', 'r')
    
    contenido = archivo_origen.read()
    
    archivo_destino = open('nombre_del_archivo_destino.txt', 'w')
    
    archivo_destino.write(contenido)
    
except Exception as e:
    print(f"Ocurrió un error: {e}")
    
finally:
    archivo_origen.close()
    archivo_destino.close()
    print("Los archivos se han cerrado correctamente.")
