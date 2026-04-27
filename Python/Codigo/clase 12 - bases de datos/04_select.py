import sqlite3
ruta_db = "C:/Users/Willy/Documents/Repositorios/Programaci-n/Python/Codigo/clase 12 - bases de datos/database/alumnos.db"

conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()

cursor.execute("SELECT * from alumno")

datos = cursor.fetchall() #fetchall significa que se ingresan a la variable todos los registros de la consulta

for fila in datos:
    print(fila)

conexion.close