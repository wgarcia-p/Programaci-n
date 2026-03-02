##programa que usa una funcion para calcular el IVA de un producto
#infinitamente

#muestra un menu para ingresar el precio
#1. Ingresar precio del producto
#2. Mostrar precio del producto con IVA
#3. Salir



def calcular_iva(precio):
    iva = precio * 0.12
    return iva

def main():
    while True:
        precio_producto = float(input("Ingrese el precio del producto: "))
        iva_producto = calcular_iva(precio_producto)
        print(f"El IVA del producto es: {iva_producto :.2f}") #:.2f muestra el resultado con 2 decimales

if __name__ == "__main__":
    main()