


lista_clientes= []
codigo = 100


def agregar_cliente(codigo,nombre,telefono,direccion,correo):
    cliente = {
          "codigo":codigo,
          "nombre":nombre,
          "telefono": telefono,
          "direccion": direccion,
          "correo":correo
    }
    lista_clientes.append(cliente)


def mostrar_clientes():
    for cliente in lista_clientes:
            print(f"Nombre: {cliente["nombre"]}, Codigo: {cliente["codigo"]}, Telefono: {cliente["telefono"]}")
    input("Espera...")

while True:
    codigo = codigo+2
    print("BIENVENIDO AL SISTEMA DE INGRESO DE CLIENTES")
    print("1. Ingresar un nuevo cliente")
    print("2. Mostrar el listado de clientes")
    print("3. Salir")
    seleccion = int(input("Seleccione una opcion\n"))
    
    
    match seleccion:
        case 1:
                codigo_cliente = codigo
                nombre_cliente=input("Ingrese el nombre del cliente\n")
                telefono_cliente = input("Ingrese el numero de telefono del cliente\n")
                direccion_cliente = input("Ingrese la direccion del cliente\n")
                correo_cliente = input("Ingrese el email del cliente\n")
                agregar_cliente(codigo_cliente,nombre_cliente,telefono_cliente,direccion_cliente,correo_cliente)

        case 2:
                if not lista_clientes:
                      print("No hay clientes registrados")
                else:
                        mostrar_clientes()
        case 3:
                print("Gracias por usar nuestro sistema")
                break