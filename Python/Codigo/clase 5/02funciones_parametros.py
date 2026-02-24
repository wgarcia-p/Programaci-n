#funcion que recibe dos numeros y los suma

def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

#llama a la funcion sumar y muestra el resultado
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
suma = sumar(numero1, numero2)
print(f"La suma de {numero1} y {numero2} es: {suma}")