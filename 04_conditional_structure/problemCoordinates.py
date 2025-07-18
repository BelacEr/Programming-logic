def ingresar_numeros(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Por favor ingresa solo números.")

def coordenadas():
    print('Determinar el cuadrante al que pertenece el punto X y Y.')
    x = ingresar_numeros('Valor de X: ')
    y = ingresar_numeros('Valor de Y: ')

    if x == 0 and y == 0:
        print('Origen')
    elif x > 0 and y == 0:
        print('Eje X')
    elif x == 0 and y > 0:
        print('Eje Y')
    elif x > 0 and y > 0:
        print('Cuadrante Q1')
    elif x < 0 and y > 0:
        print('Cuadrante Q2')
    elif x < 0 and y < 0:
        print('Cuadrante Q3')
    else:
        print('Cuadrante Q4')
    
# ejecutar programa
coordenadas()