# generador_claves.py
import random
import string

def generar_clave(longitud_clave):
    caracteres_posibles = string.ascii_letters + string.digits
    clave_generada = ''.join(random.choice(caracteres_posibles) for _ in range(longitud_clave))
    return clave_generada

# Utiliza el módulo en un programa principal
longitud_clave = 12
clave_generada = generar_clave(longitud_clave)
print(f"Clave generada: {clave_generada}")
