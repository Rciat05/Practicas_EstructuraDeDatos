#Ejercicio 3 Roberto Iglesias

def main():
    notas = []
    for i in range(5):
        nota = float(input("Ingrese la nota {} (entre 0 y 10): ".format(i + 1)))
        while nota < 0 or nota > 10:
            print("La nota debe estar entre 0 y 10.")
            nota = float(input("Ingrese la nota {} (entre 0 y 10): ".format(i + 1)))
        notas.append(nota)

    print("\nNotas obtenidas:")
    for i, nota in enumerate(notas, start=1):
        print("Nota {}: {}".format(i, nota))

    Nota_Mayor = max(notas)
    Nota_menor = min(notas)
    prom = sum(notas) / len(notas)

    print("\nMayor nota: {}".format(Nota_Mayor))
    print("Menor nota: {}".format(Nota_menor))
    print("Nota media: {:.2f}".format(prom))

if __name__ == "__main__":
    main()