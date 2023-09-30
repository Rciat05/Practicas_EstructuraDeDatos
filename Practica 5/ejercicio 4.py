#Ejercicio #4 U20230727 Roberto Iglesias

def ingresar_datos():
    n = int(input("Ingrese la cantidad de datos: "))
    datos = []
    for i in range(n):
        dato = float(input(f"Ingrese el dato {i + 1}: "))
        datos.append(dato)
    return datos


def ordenar_lista(lista):
    return sorted(lista)


def sumatoria(lista):
    return sum(lista)

def media(lista):
    sumatoria = sumatoria(lista)
    return sumatoria / len(lista)


def calcular_mediana(lista):
    lista_ordenada = ordenar_lista(lista)
    n = len(lista_ordenada)
    if n % 2 == 0:
        medio1 = lista_ordenada[n // 2 - 1]
        medio2 = lista_ordenada[n // 2]
        mediana = (medio1 + medio2) / 2
    else:
        mediana = lista_ordenada[n // 2]
    return mediana

def moda(lista):
    from collections import Counter
    conteo = Counter(lista)
    moda = [k for k, v in conteo.items() if v == max(conteo.values())]
    return moda

def desviacion_estandar(lista):
    import math
    media = media(lista)
    n = len(lista)
    suma_cuadrados = sum([(x - media) ** 2 for x in lista])
    desviacion_estandar = math.sqrt(suma_cuadrados / (n - 1))
    return desviacion_estandar


datos = ingresar_datos()
print("Datos:", datos)
print("Datos ordenados:", ordenar_lista(datos))
print("Sumatoria de datos:", sumatoria(datos))
print("Media de datos:", media(datos))
print("Mediana de datos:", calcular_mediana(datos))
print("Moda de datos:", moda(datos))
print("Desviación estándar de datos:", desviacion_estandar(datos))
