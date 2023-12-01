import re

def encontrar_ocurrencias(texto, palabra):


    patron = re.compile(r'\b' + re.escape(palabra) + r'\b', re.IGNORECASE)



    iterador_coincidencias = patron.finditer(texto)


    ubicaciones_ocurrencias = [coincidencia.span() for coincidencia in iterador_coincidencias]

    return ubicaciones_ocurrencias

texto_ejemplo = "Este es un ejemplo de texto. Este texto tiene la palabra ejemplo varias veces."

palabra_buscada = "ejemplo"

ocurrencias = encontrar_ocurrencias(texto_ejemplo, palabra_buscada)
print(ocurrencias)