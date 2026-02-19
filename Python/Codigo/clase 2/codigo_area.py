#muestra el pais de origen del codigo de area
import os
#importacion de la libreria os para limpiar la consola
def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')
    #funcion para limpiar la consola, dependiendo del sistema operativo
    #solo se escribe una vez y se llama cada vez que se quiera limpiar la consola
clrscr()
#limpiar la consola al iniciar el programa
codigo_area = input("Introduce el código de área: ")
if codigo_area == "1":
    print("El código de área 1 corresponde a Estados Unidos y Canadá")
elif codigo_area == "44":
    print("El código de área 44 corresponde a Reino Unido")
elif codigo_area == "91":
    print("El código de área 91 corresponde a India")
else:
    print("Código de área no reconocido para America")