#genera una lista

productos = ["manzana", "banana", "naranja", "pera"]

print(productos)

#accede a un elemento de la lista por su indice
print(productos[0]) #manzana
print(productos[2]) #naranja
print('accede a un elemento de la lista por su indice')

#modifica un elemento
productos[2] = "papaya"

#imprime el producto modificado
print(productos[2]) #papaya

#agrega un nuevo producto a la lista (al final)
productos.append("uva")
print(productos)

#agrega en una posicion especifica (indice 1 y el resto se corre hacia la derecha)
productos.insert(1, "fresa")
print(productos)

#elimina un producto por su indice
del productos[3] #elimina la pera

#elimina un producto por su valor (elimina la fresa)
productos.remove("fresa")
print(productos)

#recorre una lista con un ciclo for
for producto in productos:
    print(producto)
 



#funciones utilies
print(len(productos)) #cantidad de productos en la lista
print(productos.count("manzana")) #cuenta cuantas veces aparece la manzana en la lista
productos.sort() #ordena la lista alfabeticamente
print(productos)
productos.reverse() #invierte el orden de la lista
print(productos)
