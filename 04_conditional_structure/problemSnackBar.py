def ingresar_numero(datos):
    while True:
        try:
            return int(input(datos))    
        except ValueError:
            print("Error: Por favor ingresa solo números enteros.")

# Ejecutar programa


codigo = ingresar_numero('Código del producto comprado: ')
cantidad = ingresar_numero('Cantidad comprada: ')

try:
    if codigo == 1:
        precio = 5.00
    elif codigo ==  2:
        precio = 3.50
    elif codigo ==  3:
        precio = 4.80
    elif codigo ==  4:
        precio = 8.90
    elif codigo == 5:
       precio = 7.32
    else:
        print('Ingrese un código válido (del 1 al 5).')

    importe = precio * cantidad
    print(f"Importe a pagar: R$ {importe:.2f}")
except NameError:
    None
