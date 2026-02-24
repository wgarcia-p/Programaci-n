#programa que calcula el salario de un empleado



#CALCULA EL SALARIO BRUTO
def calcular_salario(horas_trabajadas, tarifa_hora):
    salario = horas_trabajadas * tarifa_hora
    return salario

#CALCULA EL DESCUENTO DEL IGSS
def igss(salario):
    descuento_igss = salario * 0.0483
    return descuento_igss


#CALCULA EL DESCUENTO DEL ISR
def isr(salario):
    if salario > 3000:
        descuento_isr = salario * 0.05
        return descuento_isr
    #DEVUELVE UN VALOR DE 0 SI EL SALARIO ES MENOR O IGUAL A 3000, YA QUE NO SE APLICA EL DESCUENTO DEL ISR
    else:
        return 0
    
#CALCULA EL SALARIO NETO DESPUÉS DE APLICAR LOS DESCUENTOS DE IGSS E ISR    
def salario_neto(salario, descuento_igss, descuento_isr):
    salario_neto = salario - (descuento_igss + descuento_isr)
    return salario_neto

#ACUMULADOR PARA EL TOTAL PAGADO EN PLANILLA
def total_pagado(planilla,total):
    total = total + planilla
    return total

#INICIA LOS PAGOS SI SE CONSULTAN ANTES DE REGISTRAR ALGÚN EMPLEADO
pagos=0
while True:
    print("1. Calcular salario del empleado ")
    print("2. Mostrar total pagado en planilla ")
    print("3. Salir ")
    opcion = int(input("Ingrese una opción: "))
    match opcion:
        case 1:
            print("Ingrese el nombre del empleado: ")
            nombre = input()
            print("Ingrese las horas trabajadas: ")
            horas = int(input())
            print("Ingrese la tarifa por hora: ")
            tarifa = float(input())
            
            salario = calcular_salario(horas, tarifa)
            #CALCULA EL SALARIO BRUTO

            descuento_igss = igss(salario)
            #CALCULA EL DESCUENTO DEL IGSS

            descuento_isr = isr(salario)
            #CALCULA EL DESCUENTO DEL ISR

            salario_final = salario_neto(salario, descuento_igss, descuento_isr)

                #CALCULA EL SALARIO NETO DESPUÉS DE APLICAR LOS DESCUENTOS DE IGSS E ISR

            print(f"El salario bruto de {nombre} es: Q{salario}")
                #IMPRIME EL SALARIO BRUTO DEL EMPLEADO
            
            print(f"El total de descuentos aplicados es: Q{descuento_igss + descuento_isr}")
                #IMPRIME EL TOTAL DE DESCUENTOS APLICADOS

            print(f"El salario neto de {nombre} es: Q{salario_final}")
                #IMPRIME EL SALARIO NETO DEL EMPLEADO
            
            pagos = total_pagado(salario_final, pagos)
                #ACUMULA EL SALARIO NETO DEL EMPLEADO AL TOTAL PAGADO EN PLANILLA
            input("Presione Enter para continuar...")
        case 2:
            print(f"El total pagado en planilla es: Q{pagos}")
            input("Presione Enter para continuar...")
        case 3:
            print("Gracias por usar el sistema de cálculo de salarios.")
            break
        case _:            print("Opción no válida, por favor seleccione una opción del menú.")
        
