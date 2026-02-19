#el programa comprueba si aprobo la clase
import os
#importacion de la libreria os para limpiar la consola

def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')
    #funcion para limpiar la consola, dependiendo del sistema operativo
    #solo se escribe una vez y se llama cada vez que se quiera limpiar la consola

clrscr()
#limpiar la consola al iniciar el programa
nota = int(input("¿Cuál es tu nota? "))
if nota >= 70:
    print("Aprobaste la clase")
else:
    print("No aprobaste la clase")