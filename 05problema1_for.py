#programa que solicita un numero y muestra su tabla de multiplicar del 1 al 10


# input siempre devuelve un string, por lo que es necesario convertirlo a entero usando int() para poder realizar operaciones matemáticas
numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
print("Tabla de multiplicar del", numero)
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)

print("¡Gracias por usar el programa de tablas de multiplicar!")

