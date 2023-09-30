class Estudiante:
    def __init__(self, nombre, apellido, carnet, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.carrera = carrera

estudiante1 = Estudiante("Roberto", "Iglesias", "U20230727", "Tec. Desarrollo de software")
print(f'Nombre: {estudiante1.nombre}, Apellido: {estudiante1.apellido}, Carnet: {estudiante1.carnet}, Carrera: {estudiante1.carrera}')


