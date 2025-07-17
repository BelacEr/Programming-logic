def encontrar_mayor():
    print('Introduzca las tres distancias: ')
    
    try:
        num1 = float(input('Primera distancia: '))
        num2 = float(input('Segunda distancia: '))
        num3 = float(input('Tercera distancia: '))
                
        mayor = num1

        if num1 < num2:
            mayor = num2
        if num1 < num3:
            mayor = num3

        print(f"DISTANCIA MÁS LARGA: {mayor:.2f}")

    except ValueError:
        print("Error: Debes ingresar un número válido. Inténtalo de nuevo.")
    
encontrar_mayor()