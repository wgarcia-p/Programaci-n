import sqlite3
ruta_db = "C:/Users/Willy/Desktop/PreLab_Willy/database/db_multas.db"

conexion = sqlite3.connect(ruta_db)

print("Base de datos conectada")

conexion.close()