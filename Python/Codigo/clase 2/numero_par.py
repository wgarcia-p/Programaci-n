#programa que comprueba si un numero es par o impar

import os
#importacion de la libreria os para limpiar la consola

def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')
    #funcion para limpiar la consola, dependiendo del sistema operativo
    #solo se escribe una vez y se llama cada vez que se quiera limpiar la consola
clrscr()
#limpiar la consola al iniciar el programa

numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")