def ingresar_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada fallida. Por favor, asegúrate de solo ingresar números.")


precio = ingresar_numero('Precio unitario del producto: ')
cantidad  = ingresar_numero('Cantidad comprada: ')
dinero = ingresar_numero('Dinero recibido: ')

print(f"El cambio es de: {dinero - precio * cantidad}")