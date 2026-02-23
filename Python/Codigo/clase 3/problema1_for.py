#Sumar los primeros 20 números naturales

#Crea un programa que use un ciclo for para calcular la 
#suma de los números del 1 al 20 y 
#muestre el resultado final en pantalla.

suma = 0

for contador in range(1, 21):
    suma += contador
    #el operador += es una forma abreviada de escribir 
    # suma = suma + contador
print("La suma de los primeros 20 números naturales es:", suma)