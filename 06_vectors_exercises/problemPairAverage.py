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
    N = ingresar_numero('¿Cuántos elementos tendrá el vector? ', tipo='int')
    vector = []
    pares = []
    
    for num in range(N):
        vector.append(ingresar_numero('Introduzca un número: '))
        if vector[num] % 2 == 0:
            pares.append(vector[num])
    
    print('-' * 30)
    if not pares:
        print("NINGÚN NÚMERO PAR.")
    else:
        media_pares = sum(pares) / len(pares)
        print(f'MEDIA DE PARES: {media_pares:.1f}')

if __name__ == '__main__':
    main()