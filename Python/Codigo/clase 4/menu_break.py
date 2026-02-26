#programa que muestra un menu
#hasta que el usuario decida salir
#rompe el ciclo while con break

opcion = 0
while True:
    print("Bienvenido al sistema")
    print("1. Opcion 1")
    print("2. Opcion 2")
    print("3. Salir")
    opcion = int(input("Selecciona una opcion: "))
    match (opcion):
        case 1:
            print("Has seleccionado la opcion 1")
            input("Presiona Enter para continuar...")
        case 2:
            print("Has seleccionado la opcion 2")
            input("Presiona Enter para continuar...")
        case 3:
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion no valida")

print("Fin del programa")
input("Presiona Enter para salir...")