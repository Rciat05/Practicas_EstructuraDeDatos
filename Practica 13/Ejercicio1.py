class Biblioteca:
    def __init__(self):
        self.pila_libros = []

    def prestar_libro(self, libro):
        if libro not in self.pila_libros:
            self.pila_libros.append(libro)
            print(f'Libro "{libro}" prestado con éxito.')
        else:
            print(f'El libro "{libro}" ya está prestado.')

    def devolver_libro(self, libro):
        if libro in self.pila_libros:
            self.pila_libros.remove(libro)
            print(f'Libro "{libro}" devuelto correctamente.')
        else:
            print(f'¡Error! El libro "{libro}" no está en préstamo.')

    def mostrar_estado(self):
        if not self.pila_libros:
            print('La biblioteca está vacía.')
        else:
            print('Libros en préstamo:')
            for libro in self.pila_libros:
                print(f' - {libro}')

# Crear instancia de la clase Biblioteca
biblioteca = Biblioteca()

# Operaciones de préstamo y devolución con libros específicos
biblioteca.mostrar_estado()

libros_a_prestar = ["Cien años de soledad", "Don Quijote de la Mancha", "1984", "Harry Potter y la piedra filosofal"]
for libro in libros_a_prestar:
    biblioteca.prestar_libro(libro)

biblioteca.mostrar_estado()

libro_a_devolver = "Cien años de soledad"
biblioteca.devolver_libro(libro_a_devolver)

biblioteca.mostrar_estado()
