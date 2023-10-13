
nombres = []
while True:
    nombre = input("Ingresa un nombre (o pulsa Enter para terminar): ")
    if nombre == "":
        break
    nombres.append(nombre)

with open("nombres.txt", "w") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")

print("Nombres guardados en 'nombres.txt'")
