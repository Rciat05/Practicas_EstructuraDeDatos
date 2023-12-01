import re

def contiene_fecha_valida(cadena):
    # Define el patrón para la fecha en formato "dd/mm/yyyy"
    patron_fecha = re.compile(r'\b\d{2}/\d{2}/\d{4}\b')

    # Usa la función search para buscar la presencia del patrón en la cadena
    coincidencia = patron_fecha.search(cadena)

    # Devuelve True si hay al menos una fecha válida, False en caso contrario
    return bool(coincidencia)

# Ejemplos de uso:
cadena_1 = "Hoy es 30/11/2023 y mañana será 01/12/2023."
cadena_2 = "No hay fechas aquí."

print(contiene_fecha_valida(cadena_1))  # True
print(contiene_fecha_valida(cadena_2))  # False