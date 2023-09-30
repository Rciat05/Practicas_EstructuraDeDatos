#Ejercio de tarea #2 Roberto Carlos Iglesias Álvarez

numero = float(input("Por favor ingrese su número: "))
minimo = int(input("Desde donde desea comenzar? "))
maximo = int(input("Donde desea terminar? "))

for contador in range(minimo, maximo+1):
    producto = numero * contador
    print("{0} x {1} = {2} " .format (numero, contador, producto) )