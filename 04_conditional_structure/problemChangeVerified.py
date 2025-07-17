def ingresar_numero(mensaje, tipo='float'): # Comprobar que precio y dinero sean float y cantidad int
    while True:
        entrada = input(mensaje)
        try:
            if tipo == 'float':
                return float(entrada)
            elif tipo == 'int':
                return int(entrada)
        except ValueError:
            tipo_mensaje = 'decimal' if tipo == 'float' else 'entero'
            print(f"¡Error! Debes ingresar un número {tipo_mensaje} válido. Inténtalo de nuevo.")

print('El programa debe mostrar la cantidad de cambio que debe devolverse al cliente.')
precio = ingresar_numero('Precio unitario del producto: ', 'float') # float
cantidad = ingresar_numero('Cantidad comprada: ', 'int')            # int
dinero = ingresar_numero('Dinero recibido: ', 'float')              # flaot

# Calcular el cambio
total = precio * cantidad
if dinero < total:
    falta = dinero - total
    print(f"DINERO INSUFICIENTE, FALTAN: {abs(falta):.2f}")
else:   # dinero > total
    cambio = dinero - total
    print(f"El cambio es {cambio:.2f}")

