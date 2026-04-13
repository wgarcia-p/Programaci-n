#imprime un reporte


productos = [
    {"nombre": "Laptop", "precio": 750, "stock": 5},
    {"nombre": "Mouse", "precio": 25, "stock": 20}
]

with open("reporte.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"Nombre: {p['nombre']}\n")
        archivo.write(f"Precio: Q{p['precio']}\n")
        archivo.write(f"Stock: {p['stock']}\n")
        archivo.write("------------------------\n")

print("Archivo generado.")