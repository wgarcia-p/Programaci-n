#diccionario que describe a un estudiante

estudiante = {
    "codigo" : "5BC01",
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 17,
    "carrera": "Bachillerato en computacion",
 }


print(estudiante["carrera"])

#modificar el valor de un diccionario

estudiante["nombre"] = "Luis Fernando"
print(estudiante["nombre"])

#agregar una clave:valor al diccionario
estudiante["email"] = 'luisf@gmail.com'
print(estudiante)

#borrar un clave:valor
del estudiante["edad"]
print(estudiante) 

#recorrer las claves
for clave in estudiante:
    print(clave)

#recorrer los valores
for valor in estudiante.values():
    print(valor)

