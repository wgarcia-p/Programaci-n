import sqlite3
#C:/Users/Willy/Documents/Repositorios/Programaci-n/Python/Codigo/clase 12 - bases de datos/database/alumnos.db
ruta_db = "C:/Users/Willy/Documents/Repositorios/Programaci-n/Python/Codigo/clase 12 - bases de datos/database/alumnos.db"

conexion = sqlite3.connect(ruta_db)

print("Base de datos conectada")

conexion.close()