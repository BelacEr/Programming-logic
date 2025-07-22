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
    N = ingresar_numero('¿Cuántos alumnos ingresarán? ', tipo='int')
    vector_nombre = []
    promedios = []

    for i in range(N):
        print(f'\nIntroduzca el nombre, la primera y la segunda nota del {i + 1}° alumno.')
        nombre = input('Nombre: ')
        nota1 = ingresar_numero('Primera nota: ')
        nota2 = ingresar_numero('Segunda nota: ')
        promedio = (nota1 + nota2) / 2

        vector_nombre.append(nombre)
        promedios.append(promedio)
        print('-' * 30)

    print('\nALUMNOS APROBADOS:')
    for i in range(N):
        if promedios[i] >= 6.0:
            print(f'{vector_nombre[i]} con promedio {promedios[i]:.2f}')

if __name__ == '__main__':
    main()