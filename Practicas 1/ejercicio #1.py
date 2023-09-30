#ejercicio numero 1 Roberto Iglesias

def metros_a_kilometros(metros):
    kilometros = metros / 1000
    return kilometros

metros = float(input("Ingresa la cantidad en metros: "))

kilometros = metros_a_kilometros(metros)

print(f"{metros} metros son {kilometros} kilómetros")