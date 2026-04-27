from datetime import datetime

lista_clientes= []
ruta_recibos = "C:/Users/Willy/Documents/Repositorios/Programaci-n/Python/Codigo/sistema_bancario/recibos/clientes.txt"

def insertar_clientes():

      cliente1 = {
            "codigo":100,
            "nombre":"Juan Perez",
            "telefono": "123456789",
            "direccion": "Calle 123",
            "correo": "juan.perez@example.com",
            "saldo": 1000.0
      }
      lista_clientes.append(cliente1)
      cliente2 = {
            "codigo":120,
            "nombre":"María García",
            "telefono": "987654321",
            "direccion": "Avenida 456",
            "correo": "maria.garcia@example.com",
            "saldo": 1000.0
      }
      lista_clientes.append(cliente2)
      cliente3= {
            "codigo":130,
            "nombre":"Carlos López",
            "telefono": "123456789",
            "direccion": "Calle 123",
            "correo": "carlos.lopez@example.com",
            "saldo": 10.0
      }
      lista_clientes.append(cliente3)

      cliente4 = {
            "codigo":140,
            "nombre":"Sofía Martínez",
            "telefono": "123456789",
            "direccion": "Calle 123",
            "correo": "sofia.martinez@example.com",
            "saldo": 1050.0
      }
      lista_clientes.append(cliente4)

      cliente5 = {
            "codigo":150,
            "nombre":"Juan Perez",
            "telefono": "123456789",
            "direccion": "Calle 123",
            "correo": "juan.perez@example.com",
            "saldo": 1000.0
      }
      lista_clientes.append(cliente5)
codigo = 160
insertar_clientes()

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
    
    ahora = datetime.now()
    with open(ruta_recibos, "w") as archivo:
          archivo.write(" ")
    for cliente in lista_clientes:
        print(f"Nombre: {cliente['nombre']}, Codigo: {cliente['codigo']}, Telefono: {cliente['telefono']}, Saldo: {cliente['saldo']}")
    impresion = input("Desea imprimir el listado de clientes S/N?")
    if impresion.upper() == "S":
          for cliente in lista_clientes:
            texto =(
            "============ REGISTRO ====================\n"
            f"Nombre: {cliente['nombre']}, Codigo: {cliente['codigo']}, Telefono: {cliente['telefono']}, Saldo: {cliente['saldo']}\n"
            "==========================================\n"
            )
#C:\Users\Willy\Documents\Repositorios\Programaci-n\Python\Codigo\sistema_bancario\recibos
            with open(ruta_recibos, "a") as archivo:
                  archivo.write(f"{texto}\n")
          with open(ruta_recibos,"a") as archivo:
            archivo.write(f"Fecha y hora de impresión: {ahora.strftime("%d/%m/%Y %H:%M")}")
          input("Impresion exitosa, presione enter para continuar")
    else:
        print("Regresando al menu principal...")    
def depositos(codigo_cliente):
    print("DEPOSITOS A CUENTAS")
    cuenta_deposito = codigo_cliente
    for clientes in lista_clientes:
          if clientes["codigo"] == cuenta_deposito:
                deposito = float(input("Ingrese el monto a acreditar\n"))
                saldo_anterior = clientes["saldo"]
                if deposito > 0:
                    clientes["saldo"] = deposito+saldo_anterior
                    print("Depósito ingresado con éxito\n")
                    input("Presione enter para contiuar")
                    break
                else:
                    print("Monto no válido, el depósito debe ser mayor a 0")
                    input("Presione enter para continuar")
                    break
                
    else:
          print("Cuenta no encontrada")
          input("Regresando al menu principal...")
    
def retiros(codigo_cliente):
      print("Retiros de cuentas")
      cuenta_retiro = codigo_cliente
      for clientes in lista_clientes:
            if clientes["codigo"] == cuenta_retiro:
                retiro = float(input("Ingrese el monto que desea retirar"))
                saldo_anterior = clientes["saldo"]
                if saldo_anterior - retiro >= 0:
                    clientes["saldo"] = saldo_anterior - retiro
                    print("Transacción finalizada")
                    input("Presione enter para contiuar")
                else:
                  print("Saldo insuficiente en la cuenta")
                  input("Presione enter para continuar")
                  break
            else:
                  print("Cuenta no encontrada")
                  input("Presione enter para continuar")

def consulta(codigo_cliente):
      ahora = datetime.now().strftime("%d-%m-%Y HH %H-%M-%S")
      print("Consulta de estado de cuenta")
      cuenta_consulta = codigo_cliente
      for clientes in lista_clientes:
            if clientes["codigo"] == cuenta_consulta:
                  texto=(
                  "============ ESTADO DE CUENTA ====================\n"
                  f"| Nombre: {clientes['nombre']},\n| Codigo: {clientes['codigo']},\n| Telefono: {clientes['telefono']},\n| Saldo: {clientes['saldo']}\n"
                  "==========================================\n"
                  )
                  with open(f"C:/Users/Willy/Documents/Repositorios/Programaci-n/Python/Codigo/sistema_bancario/estados de cuenta/{clientes['codigo']}-{ahora}.txt", "a") as archivo:
                        archivo.write(f"{texto}\n")
                  print("El estado de cuenta se ha impreso exitosamente!")
                  input("Presione enter para continuar")
                  break
                  


      else:
            print("Cuenta no encontrada")
            input("Presione enter para continuar")                     

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
                print("Depositos a cuentas")
                cuenta_deposito = int(input("Ingrese la cuenta a acreditar\n"))
                depositos(cuenta_deposito)        
        case 4:
                print("Retiros de cuentas")
                cuenta_retiro = int(input("Ingrese la cuenta a debitar\n"))
                retiros(cuenta_retiro)
        case 5:
                print("Consulta de estado de cuenta")
                cuenta_consulta = int(input("Ingrese la cuenta a consultar\n"))
                consulta(cuenta_consulta)
        case 6:
                print("Gracias por usar el sistema del banco LMG")
                input("Presione enter para salir")
                break
        case _:
                print("Opción no válida")