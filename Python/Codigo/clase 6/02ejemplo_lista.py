#una tienda necesita registrar los productos vendidos hoy

#creamos la lista
ventas = []

#registramos las ventas
ventas.append("computadora")
ventas.append("telefono")
ventas.append("tablet")

print('Productos vendidos hoy:')
for producto in ventas:
    print(producto)

print('Cantidad de productos vendidos hoy:', len(ventas))