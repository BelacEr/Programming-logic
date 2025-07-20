def ingresar_numeros(mensaje, tipo='float'):
    while True:
        try:
            entrada = input(mensaje)
            if tipo == 'int':
                return int(entrada)
            return float(entrada)
        except:
            print("Error: Ingresa un número válido.")

def main():
    n = ingresar_numeros('¿Cuántos números vas a escribir? ', tipo='int')
    vector = []
    
    for _ in range(n):
        vector.append(ingresar_numeros('Escribe un número: '))

    suma = sum(vector)
    media = suma / len(vector)

    print(f"VALORES: ",*vector, sep=' ')
    print(f"SUMA: {suma:.2f}")
    print(f"MEDIA: {media:.2f}")

if __name__ == '__main__':
    main()
