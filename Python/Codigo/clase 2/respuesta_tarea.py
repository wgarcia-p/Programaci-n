#programa que usa case
#para encontrar el pais
#segun el codigo de area


# Variable de entrada
codigo_area = int(input("Introduce un código de área en Ámerica: "))

# Uso de match-case (Python 3.10+)
match codigo_area:
    case 1:
        print("Estados Unidos")
    case 52:
        print("México")
    case 57:
        print("Colombia")
    case 58:
        print("Venezuela")
    case _:
        print("Código de área no reconocido")