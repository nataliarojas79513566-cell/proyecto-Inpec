class Preso:
    def __init__(self, nombre, turno, zona):
        self.nombre = nombre
        self.turno = turno
        self.zona = zona

    def __str__(self):
        return f"Preso: {self.nombre} | Turno: {self.turno} | Zona: {self.zona}"


class Nodo:
    def __init__(self, preso):
        self.preso = preso
        self.siguiente = None
        self.anterior = None


class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar(self, preso):
        nuevo = Nodo(preso)

        if self.cabeza == None:
            self.cabeza = nuevo
            self.cola = nuevo
            print("preso agregado")
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
            print("preso agregado")

    def buscar(self, nombre):
        if self.cabeza == None:
            print("la lista esta vacia")
            return

        actual = self.cabeza
        posicion = 1
        encontrado = False

        while actual:
            if actual.preso.nombre.lower() == nombre.lower():
                print(f"\n✓ Preso encontrado en posición {posicion}:")
                print(f"  Nombre: {actual.preso.nombre}")
                print(f"  Turno: {actual.preso.turno}")
                print(f"  Zona: {actual.preso.zona}")
                encontrado = True
            actual = actual.siguiente
            posicion += 1

        if not encontrado:
            print(f"No se encontró al preso '{nombre}'")

    def eliminar(self, nombre):
        if self.cabeza == None:
            print("lista vacia")
            return

        actual = self.cabeza

        while actual:
            if actual.preso.nombre.lower() == nombre.lower():
                if actual == self.cabeza and actual.siguiente is None:
                    self.cabeza = None
                    self.cola = None
                    print(f"\n ✓ Preso {nombre} eliminado correctamente")

                elif actual == self.cabeza:
                    self.cabeza = actual.siguiente
                    self.cabeza.anterior = None
                    print(f"✓ Preso {nombre} eliminado correctamente")

                elif actual.siguiente is None:
                    actual.anterior.siguiente = None
                    self.cola = actual.anterior
                    print(f" Preso {nombre} eliminado correctamente")

                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    print(f"✓ Preso {nombre} eliminado correctamente")

                return

            actual = actual.siguiente

        print(f"\n No se encontró al preso '{nombre}' para eliminar")

    def mostrar(self):
        if self.cabeza is None:
            print("No hay presos en el sistema")
            return

        actual = self.cabeza
        contador = 1

        while actual:
            print(f"{contador}. {actual.preso.nombre}")
            print(f"   Turno: {actual.preso.turno}")
            print(f"   Zona: {actual.preso.zona}")
            print("")

            actual = actual.siguiente
            contador += 1

        print(f"Total: {contador - 1} presos")

#lista = ListaDoble()
#p1 = Preso("Juan", "6:00 AM", "Zona Norte")
#lista.insertar(p1)
#lista.mostrar()