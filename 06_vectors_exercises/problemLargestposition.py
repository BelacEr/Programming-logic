def ingresar_numero(mensaje, tipo='float'):
    while True:
        try:
            entrada = input(mensaje)
            if tipo == 'int':
                return int(entrada)
            return float(entrada)
        except ValueError:
            print("Error: Ingresa un número válido.")
    
def main():
    N = ingresar_numero('¿Cuántos números vas a introducir? ', tipo='int')
    vector = []

    for _ in range(N):
        vector.append(ingresar_numero('Introduzca un número: '))

    print('-' * 30)
    valor_alto = max(vector)
    index_alto = vector.index(valor_alto)
    print(f"VALOR MÁS ALTO: {valor_alto}.")
    print(f"POSICIÓN DEL VALOR MÁS ALTO: {index_alto}")

if __name__ == '__main__':
    main()