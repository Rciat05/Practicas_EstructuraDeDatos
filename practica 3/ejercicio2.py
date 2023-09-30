#Ejercicio 2 Roberto Iglesias

def main():
    chain = input("Ingresa una oracion: ")
    lista = chain.split()  
    cantidad_palabras = len(lista)
    
    print("La cadena contiene {} palabra(s).".format(cantidad_palabras))
    print("Lista de palabras:", lista)

if __name__ == "__main__":
    main()
