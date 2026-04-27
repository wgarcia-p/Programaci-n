while True:
    try:
        numero1 = int(input("Ingrese el primer numero\n"))
        numero2 = int(input("Ingrese el  segundo\n"))
        numero3 = int(input("Ingrese el  tercero\n"))
        numero4 = int(input("Ingrese el  cuarto\n"))
        numero5 = int(input("Ingrese el  quinto\n"))
        promedio = (numero1+numero2+numero3+numero4+numero5)/5
        print(f"El promedio de los numeros es {promedio}")
        input("Presione enter para continuar...")

    except:
        print("Solo ingresar números")