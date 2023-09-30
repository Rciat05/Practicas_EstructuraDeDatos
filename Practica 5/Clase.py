 #Ejemplo de clase

#1. Crear una funcion

# Palabra reservada def seguido del nombre de la función 

from this import d


def miFunción():
    print("Este es un mensaje")



miFunción()

# 2. Funciones con parametros 

def miFuncion2(nombre, apellido ):
    print(f"Hola, {nombre} {apellido}!!")


miFuncion2('Roberto','Iglesias')

# 3. Retornar valores a traves de una función

def sumar(a,b):
    return a + b

resultado = sumar (4,6)
print(f"El resultado es {resultado}")
print(f"El resultado es {sumar(5,6)}")


# 4. Parametros (por nombre y por posición)

def AreaTriangulo(base, altura):
    return (base * altura)/ 2

alturaTriangulo = 10
baseTriangulo = 20

# ----Por posición---- 
print (AreaTriangulo(altura = alturaTriangulo, base = baseTriangulo))

# 5. Valores por defecto

def multiplicar (a, b):
    return a * b

print(f"La multiplicación es: {multiplicar (2,5)}")



#6 argumentos indeterminados  por posición 

def multiplicarMuchos (a, *numeros):
    resultados = 1
    for numero in numeros:
        a *= numero

    return a

print(multiplicarMuchos(2))
print(multiplicarMuchos(2,3)) 
print(multiplicarMuchos(2,3,4)) 

# 7. otra forma de argumentos indeterminados por nombre 

def mostrarInformación(**persona):
    información = persona.items()
    for clave, valor in información:
        print(f"{clave}: {valor}")


mostrarInformación(
    Nombre = 'Roberto Carlos',
    Apellido = 'Iglesias Álvarez')


#8 Retorno de multiples valores 
def datos():
    return "Roberto", "Iglesias", 18, 'Masculino'

misDatos = datos()

print(misDatos[0])






































































































































































































































































































