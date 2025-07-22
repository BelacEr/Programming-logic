def ingresar_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número válido.")

def main():
    N = ingresar_numero('¿Cuántas personas vas a escribir? ')
    vector_nombre = []
    vector_edad = []

    for i in range(N): 
        print(f'Datos de la {i + 1}ª persona:') 
        vector_nombre.append(input('Nombre: ').title())
        vector_edad.append(ingresar_numero('Edad: '))
        print('-' * 36)

    # Cálculos
    edad_maxima = max(vector_edad)
    indice_mayor = vector_edad.index(edad_maxima)

    # Resultados
    print(f'PERSONA MÁS VIEJA: {vector_nombre[indice_mayor]} con {edad_maxima} años.')

if __name__ == '__main__':
    main()
