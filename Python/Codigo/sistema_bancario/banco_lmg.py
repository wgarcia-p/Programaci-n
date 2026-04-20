


lista_clientes= []
codigo = 1000000


def agregar_cliente(codigo,nombre,telefono,direccion,correo,saldo):
    cliente = {
          "codigo":codigo,
          "nombre":nombre,
          "telefono": telefono,
          "direccion": direccion,
          "correo":correo,
          "saldo":saldo
    }
    lista_clientes.append(cliente)


def mostrar_clientes():
    for cliente in lista_clientes:
            print(f"Nombre: {cliente["nombre"]}, Codigo: {cliente["codigo"]}, Telefono: {cliente["telefono"]}, Saldo: {cliente["saldo"]}")
    input("Desea imprimir el listado de clientes S/N?")


while True:
    codigo = codigo+5
    print("BIENVENIDO AL BANCO LMG")
    print("1. REGISTRAR UN NUEVO CUENTAHABIENTE")
    print("2. Mostrar el listado de cuentas")
    print("3. Realizar un deposito")
    print("4. Realizar un retiro")
    print("5. Consultar estado de cuenta")
    print("6. Salir")
    seleccion = int(input("Seleccione una opcion\n"))
    
    
    match seleccion:
        case 1:
                codigo_cliente = codigo
                nombre_cliente=input("Ingrese el nombre del cliente\n")
                telefono_cliente = input("Ingrese el numero de telefono del cliente\n")
                direccion_cliente = input("Ingrese la direccion del cliente\n")
                correo_cliente = input("Ingrese el email del cliente\n")
                saldo = float(input("Ingrese monto de apertura\n"))
                agregar_cliente(codigo_cliente,nombre_cliente,telefono_cliente,direccion_cliente,correo_cliente,saldo)

        case 2:
                if not lista_clientes:
                      print("No hay clientes registrados")
                else:
                        mostrar_clientes()
        case 3:
                print("DEPOSITOS A CUENTAS")
                cuenta_deposito = int(input("Ingrese la cuenta a acreditar\n"))
                for clientes in lista_clientes:
                      if clientes["codigo"] == cuenta_deposito:
                            deposito = float(input("Ingrese el monto a acreditar\n"))
                            saldo_anterior = clientes["saldo"]
                            clientes["saldo"] = deposito+saldo_anterior
                            print("Depósito ingresado con éxito\n")
                            break
                else:
                      print("Cuenta no encontrada")
                      input("Regresando al menu principal...")
                      