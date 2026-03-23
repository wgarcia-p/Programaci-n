#crea una lista de diccionarios

productos = [
    {"nombre":"Laptop","precio":2000},
    {"nombre":"Mouse","precio":250},
    {"nombre":"Monitor","precio":1500}
]

print(productos[1])


#crear un programa que utilice una funcion para agregar productos a una lista
#el producto debe ser un diccionario con 5 claves
#para despues mostrarlo

for producto in productos:
    print(producto["nombre"], producto["precio"])

print("Bienvenido al sistema de ingreso de productos")
for i in range (3,10):
    nuevo_nombre = input("Ingrese el nombre ")
    nuevo_precio = int(input("Ingrese el nuevo precio "))
    nuevo_producto = {"nombre":nuevo_nombre,"precio":nuevo_precio}
    productos.append(nuevo_producto)
    for producto in productos:
        print(producto["nombre"], producto["precio"])
    

print("Buscar un producto por su codigo")
busqueda = input("Ingrese el nombre del producto ")
for producto in productos:
    if producto["nombre"] == busqueda:
        print(f"Producto encontrado {producto['nombre']}, con un precio de {producto['precio']}")