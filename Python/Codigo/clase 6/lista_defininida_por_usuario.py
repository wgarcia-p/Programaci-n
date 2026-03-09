#crea una lista, la llena con 5 datos definidos
#  por el usuario y luego muestra la lista

def main():
    nombres = [] #crea una lista vacia
    for i in range(5): #repite 5 veces
        nombres.append(input("Ingrese un nombre: ")) #agrega un nombre a la lista
    print(f"Los nombres ingresados son: {nombres}")

if __name__ == "__main__":
    main() #llama a la funcion main para ejecutar el programa
