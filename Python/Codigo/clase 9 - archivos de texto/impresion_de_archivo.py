#programa que crea un archivo de texto y escribe sobre el


with open("archivo.txt", "w") as archivo:
    archivo.write("Este es un archivo de texto\ncon varias lineas\ndel curso Laboratorio II")


# w - escribe (sobreescribe el archivo )
# \ (barra invertida) - salto de linea
# archivo.txt es el nombre del archivo a crear o modificar