from nodo import Nodo

class ListaDoble:

    def __init__(self):
        self.cabeza = None

    # INSERTAR
    def insertar(self, preso):

        nuevo = Nodo(preso)

        if self.cabeza is None:
            self.cabeza = nuevo
            print("Preso agregado correctamente")
            return

        actual = self.cabeza

        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo
        nuevo.anterior = actual

        print("Preso agregado correctamente")

    # MOSTRAR
    def mostrar(self):

        if self.cabeza is None:
            print("No hay presos registrados")
            return

        actual = self.cabeza

        while actual:
            print("-------------------")
            actual.preso.mostrar()
            actual = actual.siguiente

    # BUSCAR
    def buscar(self, nombre):

        actual = self.cabeza

        while actual:

            if actual.preso.nombre == nombre:
                print("Preso encontrado:")
                actual.preso.mostrar()
                return

            actual = actual.siguiente

        print("Preso no encontrado")

    # ELIMINAR
    def eliminar(self, nombre):

        actual = self.cabeza

        while actual:

            if actual.preso.nombre == nombre:

                # si es el primero
                if actual.anterior is None:
                    self.cabeza = actual.siguiente
                    if self.cabeza:
                        self.cabeza.anterior = None

                else:
                    actual.anterior.siguiente = actual.siguiente
                    if actual.siguiente:
                        actual.siguiente.anterior = actual.anterior

                print("Preso eliminado correctamente")
                return

            actual = actual.siguiente

        print("Preso no encontrado")