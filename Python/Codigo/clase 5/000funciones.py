 #funciones en python
type(32)
print(type(32))
type(3.14)
print(type(3.14))
type("Hola")
print(type("Hola"))
print(type(True))


numero = int(input("Ingrese un número: "))
resultado = numero/2
tipo = str(type(resultado))
if tipo == "<class 'int'>":
    print("El resultado es un número par")
    
else:    print("El resultado es un número impar")