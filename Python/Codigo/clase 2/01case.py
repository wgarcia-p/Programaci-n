# Ejemplo básico de case en Python (sin funciones)

# Variable de entrada
dia_semana = int(input("Introduce un número del 1 al 7 para el día de la semana: "))

# Uso de match-case (Python 3.10+)
match dia_semana:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Opción no válida")

