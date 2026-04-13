#imprime un archivo, usando un ciclo.



productos = [
    {"nombre": "Laptop", "precio": 750, "stock": 5},
    {"nombre": "Mouse", "precio": 25, "stock": 20}
]

with open("reporte_ciclo.txt", "w") as archivo:
    for p in productos:
        linea = f"NOMBRE:{p['nombre']} | Q{p['precio']} | STOCK {p['stock']}\n"
        archivo.write(linea)