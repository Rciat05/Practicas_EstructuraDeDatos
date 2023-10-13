try:
    # Intenta abrir un archivo que no existe
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
    print("El contenido del archivo es:")
    print(contenido)

except FileNotFoundError:
    print("El archivo no se encuentra.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
