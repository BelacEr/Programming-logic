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
    vector_notas = []
    promedio = []
    

    for i in range(N):
        print(f'Introduzca el nombre, la primera y la segunda nota del {i + 1}° alumno.')
        vector_nombre.append(input('Nombre: ')) 
        vector_notas.append(ingresar_numero('Primera nota: '))
        vector_notas.append(ingresar_numero('Segunda nota: '))
        promedio.append((vector_notas[i + i] + vector_notas[i + i + 1]) / 2) # 0,1. 2,3. 4,5. 6,7
        print('-' * 30)

    

if __name__ == '__main__':
    main()