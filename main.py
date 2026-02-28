from preso import Preso
from lista_doble import ListaDoble


# LISTAS SIMPLES
turnos = ["6:00 AM", "12:00 PM", "6:00 PM"]

zonas = [
    "Zona Norte",
    "Zona Sur",
    "Zona Centro",
    "Zona Rural"
]


lista = ListaDoble()


def mostrar_turnos():

    print("Turnos disponibles:")

    for i in range(len(turnos)):
        print(i+1, ".", turnos[i])


def mostrar_zonas():

    print("Zonas disponibles:")

    for i in range(len(zonas)):
        print(i+1, ".", zonas[i])


def menu():

    while True:

        print("\n--- SISTEMA INPEC ---")
        print("1. Añadir preso")
        print("2. Buscar preso")
        print("3. Eliminar preso")
        print("4. Mostrar presos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            nombre = input("Ingrese nombre: ")

            mostrar_turnos()
            t = int(input("Seleccione turno: ")) - 1

            mostrar_zonas()
            z = int(input("Seleccione zona: ")) - 1

            preso = Preso(nombre, turnos[t], zonas[z])

            lista.insertar(preso)

        elif opcion == "2":

            nombre = input("Ingrese nombre a buscar: ")
            lista.buscar(nombre)

        elif opcion == "3":

            nombre = input("Ingrese nombre a eliminar: ")
            lista.eliminar(nombre)

        elif opcion == "4":

            lista.mostrar()

        elif opcion == "5":

            print("Sistema finalizado")
            break

        else:
            print("Opción inválida")


menu()