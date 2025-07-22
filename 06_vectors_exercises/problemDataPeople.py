def ingresar_numero(mensaje, tipo='float'):
    while True:
        try:
            entrada = input(mensaje)
            if tipo == 'int':
                return int(entrada)
            return float(entrada)
        except ValueError:
            print("Error: Ingresa un número válido.")

def sexo_persona(mensaje):
    while True:
        entrada = input(mensaje).capitalize()
        if entrada == 'F':
            return entrada
            break
        elif entrada == 'M':
            return entrada
            break
        else:
            print('Escribe el sexo de la persona (M, F).')
            continue

def main():
    N = ingresar_numero('¿Cuántas personas se escribirán? ', tipo='int')
    altura_mujeres = []
    altura_hombres = []

    for i in range(N):
        altura = ingresar_numero(f"Altura de la {i + 1}° persona: ")
        sexo = sexo_persona(f"Sexo de la {i + 1}° persona ((M)asculino o (F)emenino): ")

        if sexo == 'F':
            altura_mujeres.append(altura)
        else:
            altura_hombres.append(altura)
        
    # Resultado
    print('\n', 'RESULTADO'.center(36, '='))
    print(f"Estatura más baja: {min(altura_hombres + altura_mujeres)}")
    print(f"Altura máxima: {max(altura_hombres + altura_mujeres)}")
    print(f"Altura media de las mujeres: {sum(altura_mujeres) / len(altura_mujeres)}")
    print(f"Número de hombres: {len(altura_hombres)}")
        
if __name__ == '__main__':
    main()