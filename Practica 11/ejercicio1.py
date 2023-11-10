
import math

def area_circulo(radio):
    return math.pi * radio**2

def perimetro_circulo(radio):
    return 2 * math.pi * radio

def area_rectangulo(longitud, altura):
    return longitud * altura

def perimetro_rectangulo(longitud, altura):
    return 2 * (longitud + altura)

def area_triangulo(base, altura):
    return 0.5 * base * altura

def perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3


# Ejemplo de círculo
radio_circulo = 5
print(f"Área del círculo con radio {radio_circulo}: {area_circulo(radio_circulo)}")
print(f"Perímetro del círculo con radio {radio_circulo}: {perimetro_circulo(radio_circulo)}\n")


# Ejemplo de rectángulo
longitud_rectangulo = 4
altura_rectangulo = 6
print(f"Área del rectángulo con longitud {longitud_rectangulo} y altura {altura_rectangulo}: {area_rectangulo(longitud_rectangulo, altura_rectangulo)}")
print(f"Perímetro del rectángulo con longitud {longitud_rectangulo} y altura {altura_rectangulo}: {perimetro_rectangulo(longitud_rectangulo, altura_rectangulo)}\n")


# Ejemplo de triángulo
base_triangulo = 3
altura_triangulo = 8
lado1_triangulo = 5
lado2_triangulo = 4
lado3_triangulo = 7

print(f"Área del triángulo con base {base_triangulo} y altura {altura_triangulo}: {area_triangulo(base_triangulo, altura_triangulo)}")
print(f"Perímetro del triángulo con lados {lado1_triangulo}, {lado2_triangulo} y {lado3_triangulo}: {perimetro_triangulo(lado1_triangulo, lado2_triangulo, lado3_triangulo)}")
