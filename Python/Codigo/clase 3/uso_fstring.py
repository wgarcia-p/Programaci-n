#uso del f-string para mostrar resultados

nombre = "Willy"
apellido = "García"
nacionalidad = "Guatemalteco"
edad = 30

#antes del f-string
print("Hola, mi nombre es " + nombre + " " + apellido + ", soy "+ nacionalidad + " y tengo " + str(edad) + " años.")
#con f-string
print(f"Hola, mi nombre es {nombre} {apellido}, soy {nacionalidad} y tengo {edad} años.")
