import sys

def ingresar_numeros(mensaje, tipo='float'):
    while True:
        try:
            entrada = input(mensaje)
            if tipo == 'int':
                return int(entrada)
            return float(entrada)
        except ValueError:
            print("Error: Ingresa un número válido.")

def main():
    N = ingresar_numeros('¿Cuántos elementos tendrá el vector? ', tipo='int')
    vector = []
    
    for _ in range(N):
        vector.append(ingresar_numeros('Introduzca un número: '))
    media_vector = sum(vector) / len(vector)
    print('-' * 36)
    print(f"MEDIA DEL VECTOR: {media_vector}")
    print(f"ELEMENTOS POR DEBAJO DE LA MEDIA: ")
    for num in range(N):
        if vector[num] < media_vector:
            print(vector[num])

if __name__ == '__main__':
    main()