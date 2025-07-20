def ingresar_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número válido.")

def main():
    N = ingresar_numero('¿Cuántos números enteros vas a escribir? ')
    vector = []
    pares = []

    for num in range(N):
        vector.append(ingresar_numero('Escribe un número: '))
        
        if vector[num] % 2 == 0:
            pares.append(vector[num])
        
    print(f"NÚMEROS PARES: ",*pares, sep=' ')
    print(f"NÚMERO DE PARES: {len(pares)}" )

if __name__ == '__main__':
    main()