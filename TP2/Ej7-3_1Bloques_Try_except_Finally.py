"""Escribe un programa que intente abrir un archivo, leer su
contenido y luego cerrarlo. Utiliza bloques try, except y finally
para asegurarte de que el archivo se cierre correctamente,
incluso si ocurre una excepción durante la lectura."""

try:
    archivo = open('nombre_del_archivo.txt', 'r')
    
    contenido = archivo.read()
    print(contenido)
    
except Exception as e:
    print(f"Ocurrió un error: {e}")
    
finally:
    archivo.close()
    print("El archivo se ha cerrado correctamente.")
