def ingresar_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número válido.")

def division(a, b):
    try:
        if b == 0:
            raise ValueError('DIVISIÓN IMPOSIBLE')
        return a / b
    except ValueError as e:
        print(e)
        return None  # Retornar None para indicar que hubo error

def main():
    cantidad = ingresar_numero('¿Cuántos casos vas a introducir? ')
    print('-' * 30)
    
    for _ in range(cantidad):
        numerador = ingresar_numero('Introduzca el numerador: ')
        denominador = ingresar_numero('Introduzca el denominador: ')

        resultado = division(numerador, denominador)
        if resultado is not None:  # Solo mostramos si no hubo error
            print(f"Resultado: {resultado:.2f}")
        print('-' * 30)

if __name__ == '__main__':
    main()