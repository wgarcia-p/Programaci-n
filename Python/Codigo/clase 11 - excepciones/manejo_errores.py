while True:
    try:
        edad = int(input("Ingrese edad: "))
        print("Edad registrada:", edad)
    except:
        print("Ingrese un numero, no letras")
           