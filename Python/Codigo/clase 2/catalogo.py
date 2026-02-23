#programa que recibe el codigo de producto y muestra el nombre y precio
#usando match case

producto = int(input("Ingrese el codigo del producto: "))

match producto:
    case 230226:
        print("Nombre del producto: Lámpara LED")
        print("Precio: Q25.99")
    case 230227:
        print("Nombre del producto: Mouse Inalámbrico")
        print("Precio: Q15.50")
    case 230228:
        print("Nombre del producto: Teclado Mecánico")
        print("Precio: Q45.00")
    case _:
        print("Producto no encontrado")