# Ciclo while para validar si una entrada es positiva

numero = int(input("Ingresa un número: "))

while numero <= 0:
    print("El número debe ser positivo.")
    numero = int(input("Ingresa un número positivo: "))

print(f"¡Gracias! {numero} es un número positivo.")