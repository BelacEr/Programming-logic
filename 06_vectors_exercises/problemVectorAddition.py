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
    N = ingresar_numero('¿Cuántos valores tendrá cada vector? ', tipo='int')
    vectorA = []
    vectorB = []
    VectorResult = []

    for _ in range(N):
        vectorA.append(ingresar_numero("Introduce los valores del vector A: "))

    print('-' * 36)
    for num in range(N):    
        vectorB.append(ingresar_numero("Introduce los valores del vector B: "))
        VectorResult.append(vectorA[num] + vectorB[num])
    
    print(f"VECTOR RESULTANTE".center(36, '='))
    for item in VectorResult:
        print(str(item).center(36, ' '))

if __name__ == '__main__':
    main()