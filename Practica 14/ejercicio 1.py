import re

def es_codigo_empleado_valido(cadena):
    # Define el patrón para el código de empleado válido
    patron_codigo_empleado = re.compile(r'^EMP\d{3}$')

    # Usa la función match para verificar si la cadena cumple con el patrón
    coincidencia = patron_codigo_empleado.match(cadena)

    # Devuelve True si hay coincidencia, False en caso contrario
    return bool(coincidencia)

# Ejemplos de uso:
codigo_empleado_1 = "EMP123"
codigo_empleado_2 = "EMP999"
codigo_empleado_3 = "EM123"  # No válido

print(es_codigo_empleado_valido(codigo_empleado_1))  # True
print(es_codigo_empleado_valido(codigo_empleado_2))  # True
print(es_codigo_empleado_valido(codigo_empleado_3))  # False
