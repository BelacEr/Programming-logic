def ingresar_numero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 4:
                print('Error: Ingresa un número válido (1, 2, 3 o 4 para parar.)')
                continue
            return valor
        except:
             print("Error: Ingresa un número válido.")

def leer_combustible(producto): 
    if producto == 1:
        combustible['Alcohol'] += 1
    elif producto == 2:
        combustible['Gasolina'] += 1
    elif producto == 3:
        combustible['Diesel'] += 1
    else:
        stop.append(None)

stop = []
combustible = {'Alcohol': 0, 'Gasolina': 0, 'Diesel': 0}

while True:
    eleccion = ingresar_numero('Introduzca código (1, 2, 3 o 4 para parar):')
    leer_combustible(eleccion)
    if None in stop:
        print(f"¡GRACIAS!\nAlcohol: {combustible['Alcohol']}\nGasolina: {combustible['Gasolina']}\nDiesel: {combustible['Diesel']}")
        break
    else:
        continue