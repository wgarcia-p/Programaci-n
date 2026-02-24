#programa que usa el ciclo while
#para mantener un menu en pantalla
#hasta que el usuario decida salir

opcion = 0
while opcion != 3:
    print("Menu:")
    print("1. Opcion 1")
    print("2. Opcion 2")
    print("3. Salir")
    opcion = int(input("Selecciona una opcion: "))

    match (opcion):
        case 1:
            print("Has seleccionado la opcion 1")
        case 2:
            print("Has seleccionado la opcion 2")
        case 3:
            print("Saliendo del programa...")
        case _:
            print("Opcion no valida, por favor selecciona una opcion del menu.")
    