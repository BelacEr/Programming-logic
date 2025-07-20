def ingresar_numeros(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número válido.")

def main():
    n = ingresar_numeros('¿Cuántos números vas a introducir? ')
    vector = []
    if 10 < n > 0:
        print('Error: Introduzca únicamente números enteros positivos no mayores que 10.')
    
    for _ in range(n):
        vector.append(ingresar_numeros('Escriba un número: '))

    print('NÚMEROS NEGATIVOS:')
    for num in vector:
        if num < 0:
            print(num)

if __name__ == '__main__':
    main()