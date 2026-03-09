#genera una lista con frutas

frutas = ["manzana", "pera", "sandia", "uva"]

print(frutas)

#accede a un elemento de la lista por su indice
print(frutas[0]) #manzana

#modifica un elemento
frutas[2] = "ciruela pasa"
#imprime el producto modificado
print(frutas)

#agrega un nuevo producto a la lista (al final)
frutas.append("coco")
print(frutas)

#agrega en una posicion especifica 
# (indice 1 y el resto se corre hacia la derecha)
frutas.insert(1, "platano")
print(frutas)

del frutas[2] #elimina la pera
print(frutas)

#funciones utilies
print(len(frutas)) #cantidad de frutas en la lista
print(frutas.count("manzana")) #cuenta cuantas veces aparece la manzana en la lista
frutas.sort() #ordena la lista alfabeticamente
print(frutas)
frutas.reverse() #invierte el orden de la lista
print(frutas)