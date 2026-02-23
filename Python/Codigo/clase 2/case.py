def evaluar_calificacion(nota):
    match nota:
        case 10 | 9:
            return "Excelente"
        case 8 | 7:
            return "Muy bien"
        case 6 | 5:
            return "Bien"
        case 4 | 3:
            return "Insuficiente"
        case _:
            return "Nota inválida"

# Ejemplo de uso
nota_evaluacion = int(input("Introduce la calificación (0-10): "))
print(evaluar_calificacion(nota_evaluacion)) 