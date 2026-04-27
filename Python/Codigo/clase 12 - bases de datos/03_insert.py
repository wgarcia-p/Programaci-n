import sqlite3

ruta_db = "C:/Users/Willy/Documents/Repositorios/Programaci-n/Python/Codigo/clase 12 - bases de datos/database/alumnos.db"

alumno ={
    "id_alumno": 3,
    "Nombre": "Oliver",
    "Calificacion": 80
}

conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()

cursor.execute("""
INSERT INTO alumno(id_alumno, nombre, calificacion)
VALUES(?,?,?)   
""", (alumno["id_alumno"],alumno["Nombre"],alumno["Calificacion"])
)

conexion.commit()
conexion.close()

print("Alumno guardado")
