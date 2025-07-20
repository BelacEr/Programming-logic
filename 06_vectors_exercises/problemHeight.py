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
    N = ingresar_numero('¿Cuántas personas se escribirán? ', tipo='int')
    personas = []

    for _ in range(N):
        nombre = input('Nombre: ').capitalize()  # Capitalizado :D
        edad = ingresar_numero('Edad: ', tipo='int')
        altura = ingresar_numero('Altura (m): ')
        personas.append({'nombre': nombre, 'edad': edad, 'altura': altura})
        print('-' * 30)

    # Cálculos
    alturas = [p['altura'] for p in personas]  # Lista de alturas
    media_altura = sum(alturas) / N

    menores = [p['nombre'] for p in personas if p['edad'] < 16]  # Nombres
    porcentaje = (len(menores) / N) * 100

    # Resultados
    print(f"\nAltura media: {media_altura:.2f} m")  
    print(f"Porcentaje de menores de 16 años: {porcentaje:.1f}%")
    if menores:
        print("Nombres de menores de 16:", ", ".join(menores))

if __name__ == '__main__':
    main()