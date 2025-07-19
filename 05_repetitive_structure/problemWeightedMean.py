def ingresar_numero(mensaje, tipo='float'):
    while True:
        entrada = input(mensaje)
        try:
            if tipo == 'int':
                return int(entrada)
            return float(entrada)
        except ValueError:
             print(f"Error: Ingresa un número {'entero' if tipo == 'int' else 'válido'}.")

def media_ponderada(a, b, c):
    # Calcula la media ponderada de tres números con pesos 2, 3 y 5 respectivamente.
    return (a * 2 + b * 3 + c * 5) / 10

def main():
    cantidad = ingresar_numero('¿Cuántos casos vas a introducir? ', tipo='int')
    print('\nIntroduzca tres número.')
    print('-' * 30)
    for _ in range(cantidad):
        num1 = ingresar_numero('Introduzca el primer número: ')
        num2 = ingresar_numero('Introduzca el segundo número: ')
        num3 = ingresar_numero('Introduzca el tercer número: ')

        resultado = media_ponderada(num1, num2, num3)
        print(f"Media ponderada: {resultado:.1f}")
        print('-' * 30)

if __name__ == '__main__':
    main()


    