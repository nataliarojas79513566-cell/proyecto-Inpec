from metodosinpec import Preso
from metodosinpec import ListaDoble

def pedir_opcion(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print("Opción fuera de rango.")
        except ValueError:
            print("Debe ingresar un número válido.")
def menu():
    print("\n---SISTEMA DE RECOLECCIÓN INPEC ---")
    print("1. Añadir preso")
    print("1. Buscar preso")
    print("1. Eliminar asignación")
    print("4. Mostrar todos")
    print("5. Salir")
    
    
lista = ListaDoble()

while True:
    menu()
    opcion = input("\n Seleccione una opción: ")
    
    if opcion == "1":
        nombre = input("\n Ingrese el nombre del preso: ")

        print("Turnos disponibles:")
        print("1. 6:00 AM")
        print("2. 12:00 PM")
        print("3. 6:00 PM")
        turno_op = pedir_opcion("Seleccione turno: ", 1, 3)

        turnos = ["6:00 AM", "12:00 PM", "6:00 PM"]
        turno = turnos[int(turno_op) - 1]

        print("Zonas disponibles:")
        print("1. Zona Norte")
        print("2. Zona Sur")
        print("3. Zona Centro")
        print("4. Zona Rural")
        zona_op = pedir_opcion("Seleccione zona: ", 1, 4)

        zonas = ["Zona Norte", "Zona Sur", "Zona Centro", "Zona Rural"]
        zona = zonas[int(zona_op) - 1]
        
        if lista.buscar(nombre):
            print("Ya existe un preso con ese nombre.")
            continue
        nuevo_preso = Preso(nombre, turno, zona)
        lista.insertar(nuevo_preso)

        print(f"\n {nombre} asignado al turno {turno} en {zona}.")
    elif opcion == "2":
        nombre = input("Ingrese el nombre a buscar: ")
        resultado = lista.buscar(nombre)

        if resultado:
            print("\n Preso encontrado:")
            print(resultado)
        else:
            print("\n Preso no encontrado.")
    elif opcion == "3":
        nombre = input("Ingrese el nombre a eliminar: ")
        eliminado = lista.eliminar(nombre)

        if eliminado:
            print("\n f Asignación de {nombre} eliminada correctamente.")
            resultado = lista.buscar(nombre)

        else:
            print("\n  No se encontró el preso.")
    elif opcion == "4":
        print("\n Buscando... \n")
        lista.mostrar()
    elif opcion == "5":
        print("\n Saliendo del sistema...")
        break
    else:
        print("\n Opción inválida.")