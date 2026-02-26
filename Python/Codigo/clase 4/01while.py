#programa que muestra el uso del ciclo while 

# se inicializa una variable contador en 1 para comenzar a mostrar la tabla de multiplicar desde el número ingresado por el usuario
contador = 1
# se solicita al usuario que ingrese un número para mostrar su tabla de multiplicar
numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
print("Tabla de multiplicar del", numero)
# se usa un ciclo while para mostrar la tabla de multiplicar del número ingresado por el
# usuario, el ciclo se ejecuta mientras el contador sea menor o igual a 10 para incluir el número 10 en la tabla de multiplicar
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    # se incrementa el contador en 1 para avanzar a la siguiente multiplicación en la tabla de multiplicar
    contador += 1
    