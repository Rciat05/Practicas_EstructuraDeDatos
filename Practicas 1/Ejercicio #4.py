#Ejercicio numero 4 Roberto Iglesias

numeros = []

for i in range (0,5):
    numero = float(input("Ingrese su numero: "))
    numeros.append(numero)

for i in range (0, len(numeros)):
    for j in range (0, len(numeros)-1 ):
        if numeros [j] > numeros [j+1]:
            aux = numeros [j]
            numeros [j] = numeros [j+1]
            numero [j+1] = aux
    
print (numeros) 