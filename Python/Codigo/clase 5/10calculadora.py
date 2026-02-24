#calculadora que muestra un menu de suma y resta
#usa una funcion para sumar
#usa una funcion para restar el primer numero menos segundo numero
#usa un ciclo para mostrar el menu hasta que el usuario decida salir

def sumar(num1, num2):
    resultado_suma = num1 + num2
    return resultado_suma

def restar(num1, num2):
    resultado_resta = num1 - num2
    return resultado_resta


while True:
    print("Menu:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    opcion = input("Seleccione una opcion: ")
    match opcion:
        case "1":
            numero1 = float(input("Ingrese el primer numero: "))
            numero2 = float(input("Ingrese el segundo numero: "))
            resultado = sumar(numero1, numero2)
            print(f"La suma de {numero1} y {numero2} es: {resultado}")
        case "2":
            numero1 = float(input("Ingrese el primer numero: "))
            numero2 = float(input("Ingrese el segundo numero: "))
            resultado = restar(numero1, numero2)
            print(f"La resta de {numero1} menos {numero2} es: {resultado}")
        case "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        case _:
            print("Opcion no valida. Por favor, seleccione una opcion del menu.")