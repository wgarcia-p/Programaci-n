#programa que recibe 3 numeros y calcula su promedio,
#indica si es mayor que 10, menor que 10 o igual a 10
import os

def clrscr():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

clrscr()
#limpiar la consola al iniciar el programa

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))
#leer los 3 numeros y convertirlos a float para permitir decimales
promedio = (numero1 + numero2 + numero3) / 3
#calcular el promedio sumando los 3 numeros y dividiendo entre 3
print("El promedio es:", promedio)
#imprimir el promedio calculado