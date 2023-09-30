# 2. Crear una funcion que permita calcular la raíz n de un número


def raiz(radicando, indice):
    return radicando**(1/indice)

print(f"La raiz cuadrada de 16 es: {raiz(16,2)}")
print(f"La raiz cuabica de 8 es: {raiz(8,3)}")