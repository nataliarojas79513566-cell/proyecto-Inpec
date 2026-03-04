class Preso:

    def __init__(self, nombre, turno, zona):
        self.nombre = nombre
        self.turno = turno
        self.zona = zona

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Turno:", self.turno)
        print("Zona:", self.zona)