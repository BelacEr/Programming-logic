def ingresar_numeros(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: El valor no puede ser negativo. Inténtalo de nuevo.")
                continue
            return valor
        except:
            print("Error: Por favor ingresa solo números.")

def orden():
    while True:
        x = ingresar_numeros('Ingresa el primer número: ')
        y = ingresar_numeros('Ingresa el segundo número: ')

        if x > y:
            print('Orden descendente.')
            continue
        elif x < y:
            print('Orden creciente.')
            continue
        else:       # x == y
            break
        





print('Introducir dos números.')
print('-------------------------')
orden()     # ejecutar programa