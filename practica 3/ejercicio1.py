#Ejercicio 1 Roberto Iglesias

Meses = ("Enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
tupla = tuple(Meses)

meses = int(input("Ingrese un numero del 1 al 12: "))

if 1 <= meses <= 12:
    Mes_seleccionado = Meses[meses - 1]
    print(f"El mes {meses} es {Mes_seleccionado}")
else:
    print("Numero no valido, por favor ingrese un numero entre 1-12")    

print(tupla)