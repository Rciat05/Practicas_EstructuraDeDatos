import re

def palabras_minusculas(texto):
    # Define el patrón para encontrar palabras con solo letras minúsculas
    patron_palabras = re.compile(r'\b[a-z]+\b')

    # Usa la función findall para obtener una lista de todas las palabras que cumplen con el criterio
    palabras_encontradas = patron_palabras.findall(texto)

    return palabras_encontradas

# Ejemplo de uso:
texto_ejemplo = "Este es un Ejemplo con Palabras Minúsculas y MAYÚSCULAS."

resultado = palabras_minusculas(texto_ejemplo)
print(resultado)