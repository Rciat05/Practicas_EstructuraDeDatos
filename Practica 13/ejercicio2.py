class Banco:
    def __init__(self):
        self.cola_clientes = []

    def llegada_cliente(self, cliente):
        self.cola_clientes.append(cliente)
        print(f'Cliente {cliente} llegó al banco. Actualmente hay {len(self.cola_clientes)} clientes en la cola.')

    def atender_cliente(self):
        if self.cola_clientes:
            cliente_atendido = self.cola_clientes.pop(0)
            print(f'Atendiendo al cliente {cliente_atendido}. Quedan {len(self.cola_clientes)} clientes en la cola.')
        else:
            print('No hay clientes en espera.')


banco = Banco()
banco.llegada_cliente(1)
banco.llegada_cliente(2)
banco.llegada_cliente(3)

banco.atender_cliente()
banco.atender_cliente()
banco.atender_cliente()
banco.atender_cliente()
