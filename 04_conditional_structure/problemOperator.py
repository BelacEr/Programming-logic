def ingresar_numeros(datos):    # comprueba que los datos sean números
    while True:
        try:
            return int(input(datos))
        except ValueError:
            print("¡Error! Debes ingresar un número válido. Inténtalo de nuevo.")

minutos = ingresar_numeros('Introduzca el número de minutos: ')
importe = 50.00

if minutos <= 100:
    print(f"Importe a pagar: R$ {importe:.2f}")
else:   # 103
    exceso = minutos - 100 
    importe += exceso * 2.00
    print(f"Importe a pagar: R$ {importe:.2f}")