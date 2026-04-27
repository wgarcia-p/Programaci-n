import sqlite3

ruta_db = "C:/Users/Willy/Documents/Repositorios/Programaci-n/Python/Codigo/clase 12 - bases de datos/database/alumnos.db"

conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table' AND name= 'alumno'               
               
               """)

tabla = cursor.fetchone()

if tabla:
    print("La tabla alumno existe")
else:
    print("La tabla alumno NO existe")

conexion.close()