import sqlite3
ruta_db = "C:/Users/Willy/Documents/Repositorios/Programaci-n/Python/Codigo/clase 12 - bases de datos/database/alumnos.db"
codigo=  4
while True:
    try:
        print("Menu principal")
        print("1.Insertar alumno")
        print("2.Mostrar datos")
        print("3.Salir")
        opcion = int(input("Selecione una opción \n"))

        match opcion:
            case 1:
                codigo = codigo +1
                conexion = sqlite3.connect(ruta_db)
                cursor = conexion.cursor()
                nombre = input("Ingrese el nombre del alumno")
                calificacion = input("Ingrese la calificacion")
                cursor.execute("""
                INSERT INTO alumno(id_alumno, nombre, calificacion)
                VALUES(?,?,?)   
                """, (codigo,nombre,calificacion)
                )

                conexion.commit()
                conexion.close()
                input("Se ingreso alumno con exito")

            case 2:
                conexion = sqlite3.connect(ruta_db)
                cursor = conexion.cursor()

                cursor.execute("SELECT * from alumno")

                datos = cursor.fetchall() #fetchall significa que se ingresan a la variable todos los registros de la consulta

                for fila in datos:
                    print(fila)

                conexion.close
                input("Consulta finalizada")

            case 3:
                break

            case _:
                print("Inserte una opción válida")
                input("Presione una tecla para continuar...")    


    except:
        print("Ingrese datos válidos")
        input("Presione una tecla para continuar...")