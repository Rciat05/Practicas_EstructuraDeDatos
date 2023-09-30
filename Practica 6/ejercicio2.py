#Roberto Iglesias

class CuentaUsuario:
    def __init__(self, nombre_usuario, saldo_inicial=0):
        self.nombre_usuario = nombre_usuario
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def consultar_saldo(self):
        return f'Saldo actual de {self.nombre_usuario}: ${self.saldo}'


cuenta1 = CuentaUsuario("Usuario1", 1000)
cuenta1.depositar(500)
cuenta1.retirar(200)
print(cuenta1.consultar_saldo()) 
