#crear un programa que solicite nombre, edad, fecha de nacimiento
#y muestre un mensaje con esa información
#como bienvenida a un establecimiento educativo

import os
#importacion de la libreria os para limpiar la consola

def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')
    #funcion para limpiar la consola, dependiendo del sistema operativo
    #solo se escribe una vez y se llama cada vez que se quiera limpiar la consola

clrscr()
#limpiar la consola al iniciar el programa
#llamada a la funcion clrscr() para limpiar la consola al iniciar el programa

nombre = input("¿Cuál es tu nombre? ")