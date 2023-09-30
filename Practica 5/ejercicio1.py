#1. Desarrollar un programa con una función de argumentos indeterminados que permita calcular la suma de 2 o más números.


def sumar(a,*args):
    for numero in args:
        a+=numero
    return numero

print(f"La suma es {sumar(1,2)}")
print(f"La suma es {sumar(1,2,4,4)}")
print(f"La suma es {sumar(1,2,3,5,4,6)}")