#Ejercicio 3

numeros = [1, 4, 6, 7, 8, 10, 13, 2, 9, 28, 9, 10, 7, 3, 8]
pares = []
impares = []

for numero in numeros:
    if numero%2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print ("series", numero)
print ("Pares", pares)
print ("impares", impares)