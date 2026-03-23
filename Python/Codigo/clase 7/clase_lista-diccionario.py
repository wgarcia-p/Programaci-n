productos= []

producto1 = {
    "codigo" : "5BC01",
    "nombre": "Sardina",
    "precio": 7.8
 }

productos.append(producto1)
print(productos)

producto2 = {
    "codigo" : "5BC02",
    "nombre": "Coca Cola 2 litros",
    "precio": 12
 }

producto3 = {
    "codigo" : "5BC03",
    "nombre": "Libra de azucar",
    "precio": 5
 }

productos.append(producto2)
productos.append(producto3)

print(productos)


for producto in productos:
    if producto["codigo"] == "5BC01":
        print(f"El producto es {producto["codigo"]} de nombre {producto["nombre"]}")

