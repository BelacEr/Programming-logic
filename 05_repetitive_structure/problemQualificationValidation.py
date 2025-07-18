def ingresar_numeros(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Error: El valor no puede ser negativo. Inténtalo de nuevo.")
                continue
            elif valor > 10:
                print("Error: El valor no puede ser mayor a 10. Inténtalo de nuevo.")
                continue
            return valor
        except ValueError:
            print("Error: Por favor ingresa solo números válidos.")

def calificacion():
    num1 = ingresar_numeros('Introducir primera nota: ')
    num2 = ingresar_numeros('Introducir segunda nota: ')

    media = (num1 + num2) / 2
    print(f"La media es: {media}")

calificacion()