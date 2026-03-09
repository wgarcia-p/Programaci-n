#crea un diccionario de un estudiante

estudiante = {
    "nombre": "Juan",
    "edad": 20,
    "carrera": "Bachillerato en computacion",
}

print(estudiante)
#agregar un nuevo campo al diccionario
estudiante["promedio"] = 8.5
print(estudiante)

#imprimir cada uno de los campos del diccionario
print("Nombre:", estudiante["nombre"])
print("Edad:", estudiante["edad"])
print("Carrera:", estudiante["carrera"])
print("Promedio:", estudiante["promedio"])

#modificar un campo del diccionario
estudiante["edad"] = 21
print("Edad modificada:", estudiante["edad"])

#eliminar un campo del diccionario
del estudiante["promedio"]
print(estudiante)

#recorrer las claves del diccionario
print("Claves del diccionario:")
for clave in estudiante:
    print(clave)

#recorrer los valores del diccionario
print("Valores del diccionario:")
for valor in estudiante.values():
    print(valor)

#recorrer las pares de claves y valores del diccionario
print("Pares de claves y valores del diccionario:")
for clave, valor in estudiante.items():
    print(clave, ":", valor)