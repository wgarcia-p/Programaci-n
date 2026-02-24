#funcion que recibe 5 numeros y devuelve el promedio

def promedio(num1, num2, num3, num4, num5):
    suma = num1 + num2 + num3 + num4 + num5
    promedio = suma / 5
    return promedio

#llama a la funcion promedio y muestra el resultado
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))
numero4 = float(input("Ingrese el cuarto numero: "))
numero5 = float(input("Ingrese el quinto numero: "))
promedio_resultado = promedio(numero1, numero2, numero3, numero4, numero5)
print(f"El promedio de los numeros ingresados es: {promedio_resultado}")

