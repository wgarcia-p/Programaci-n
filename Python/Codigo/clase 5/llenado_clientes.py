#programa que utiliza una funcion para
#llenar una lista
#una funcion para mostrar la lista
#y una funcion para buscar un elemento en la lista

def agregar_cliente(clientes):
    nombre = input("Ingrese el nombre del cliente:")
    clientes.append(nombre)

def mostrar_clientes(clientes):
    if len(clientes) == 0:
        print("No hay clientes registrados")
    else:
        print("Clientes registrados:")
        for cliente in clientes:
            print(cliente)
    input("Presione enter para continuar")

def renombrar_cliente(clientes):
    buscar = input("Ingrese el nombre del cliente a renombrar:")
    for cliente in clientes:
        if cliente == buscar:
            nuevo_nombre = input("Ingrese el nuevo nombre del cliente:")
            clientes[clientes.index(cliente)] = nuevo_nombre
            print("Cliente renombrado exitosamente")
            break
    else:
        print("El cliente no se encuentra registrado")
    input("Presione enter para continuar...")

def buscar_cliente(clientes):
    nombre = input("Ingrese el nombre del cliente a buscar:")
    if nombre in clientes:
        print(f"El cliente {nombre} se encuentra registrado")
    else:
        print(f"El cliente {nombre} no se encuentra registrado")
    input("Presione enter para continuar...")

def borrar_cliente(clientes):
    nombre = input("Ingrese el nombre del cliente a borrar:")
    if nombre in clientes:
        clientes.remove(nombre)
        print(f"El cliente {nombre} ha sido borrado")
    else:
        print(f"El cliente {nombre} no se encuentra registrado")




def main():
    lista_clientes = []

    while True:
        print("BIENVENIDO AL SISTEMA DE GESTION DE CLIENTES")
        print("1. Agregar cliente")
        print("2. Mostrar clientes")
        print("3. Renombrar cliente")
        print("4. Buscar cliente")
        print("5. Borrar cliente")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        match opcion:
            case "1":
                agregar_cliente(lista_clientes)
                print("Cliente agregado exitosamente")
            case "2":
                mostrar_clientes(lista_clientes)
            case "3":
                renombrar_cliente(lista_clientes)
            case "4":
                buscar_cliente(lista_clientes)
            case "5":
                borrar_cliente(lista_clientes)
            case "6":                
                print("Gracias por usar el sistema de gestion de clientes")
                break

if __name__ == "__main__":    main()