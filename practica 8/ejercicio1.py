# Abre un archivo en modo lectura
try:
    with open("archivo.txt", "r") as archivo:
        # Lee el archivo línea por línea y lo muestra en la pantalla
        for linea in archivo:
            print(linea, end='')

except FileNotFoundError:
    print("El archivo 'archivo.txt' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
