def ingresar_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada fallida. Por favor, asegúrate de solo ingresar números.")

# Uso de la función para X e Y
X = ingresar_numero('Introduce el valor de X: ')
Y = ingresar_numero('Introduce el valor de Y: ')

print(f"Suma: {X + Y}")
