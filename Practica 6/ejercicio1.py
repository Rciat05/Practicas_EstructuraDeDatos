#Roberto Iglesias 
class Articulo:
    def __init__(self, nombre, cantidad_inicial, precio):
        self.nombre = nombre
        self.cantidad = cantidad_inicial
        self.precio = precio

    def vender(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return f'Se vendieron {cantidad} {self.nombre}(s).'
        else:
            return f'No hay suficiente stock de {self.nombre} para vender {cantidad}.'

    def agregar_stock(self, cantidad):
        self.cantidad += cantidad
        return f'Se agregaron {cantidad} {self.nombre}(s) al stock.'

    def __str__(self):
        return f'{self.nombre} - Stock: {self.cantidad}, Precio: ${self.precio}'


producto1 = Articulo("Camisa", 20, 25)
print(producto1.vender(5))  
print(producto1.agregar_stock(10))  
print(producto1) 
