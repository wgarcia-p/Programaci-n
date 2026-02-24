#Una empresa llamada “Comercial El Punto” necesita un programa 
#en Python que permita al cajero registrar ventas durante el día.

#El sistema debe mostrar un menú que permanezca en pantalla 
#hasta que el usuario decida salir.


'''
MENU

1. Registrar venta
2. Mostrar total acumulado
3. Mostrar el total menos e IVA
3. Salir 

'''


def registrar_venta(nueva_venta, total_actual):
    total_actual = total_actual + nueva_venta
    return total_actual


total_dia = 0  # acumulador inicial

while True:
    print('\n¡BIENVENIDO!')
    print('1. Registrar una venta')
    print('2. Mostrar el total acumulado del día')
    print('3. Mostrar el total menos el IVA')
    print('4. Salir')

    opcion = input('Seleccione una opción: ')

    match opcion:
        case '1':
            venta_nueva = float(input('Ingrese el valor de la nueva venta: Q'))
            total_dia = registrar_venta(total_dia, venta_nueva)
            print(f'Venta registrada correctamente.')

        case '2':
            print(f'El total acumulado del día es: Q {total_dia}')
            input('Presione Enter para continuar...')

        case '3':
            print(f'El total del día menos el IVA es: Q {total_dia -(total_dia * 0.12)}')
            input('Presione Enter para continuar...')

        case '4':
            print(f'El total final del día es sin IVA es: Q {total_dia}')
            print(f'El total final del día con IVA es: Q {total_dia - (total_dia * 0.12)}')
            print('Gracias por usar el sistema de ventas.')
            break

        case _:
            print('Opción no válida, por favor seleccione una opción del menú.')