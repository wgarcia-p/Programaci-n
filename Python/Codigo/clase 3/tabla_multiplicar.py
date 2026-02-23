#Problema 3: Tabla de multiplicar de un número

#Escribe un programa que pida al usuario un número y use 
#un ciclo for para mostrar su tabla de multiplicar del 1 al 10.

#Ejemplo (si el usuario ingresa 5):
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50

numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:") 
#f string sustituye la concatenación anterior
#print("Tabla de multiplicar del " + str(numero) + ": ") <-- Concatenacion anterior
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")