#3. Crear una función que permita realizar una división en el caso de que el denominador sea 0, mostrar al usuario el mensaje “La división entre cero no está definida” caso contrario mostrar el resultado de la división.


def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return ("Error al dividir entre cero!!!!!!!!! ")


print(f"Dividir = {dividir(4,2)}")
print(f"Dividir = {dividir(4,0)}")