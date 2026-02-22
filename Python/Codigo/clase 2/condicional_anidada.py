#muestra un ejemplo de condicional anidada que clasifica
#calificaciones en A, B, C, D y F
import os
#importacion de la libreria os para limpiar la consola
def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')
    #funcion para limpiar la consola, dependiendo del sistema operativo
    #solo se escribe una vez y se llama cada vez que se quiera limpiar la consola
clrscr()
#limpiar la consola al iniciar el programa

nota = int(input("¿Cuál es tu nota? "))
if nota >= 90:
    print("Tu calificación es A")
elif nota >= 80:
    print("Tu calificación es B")
elif nota >= 70:
    print("Tu calificación es C")
elif nota >= 60:
    print("Tu calificación es D")
else:
    print("Tu calificación es F")