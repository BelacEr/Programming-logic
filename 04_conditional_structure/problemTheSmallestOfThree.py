def encontrar_menor():
    print("Ingresa tres números enteros:")
    
    try:
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        num3 = int(input("Número 3: "))
        
        menor = num1
        
        if num2 < menor:    # num2 < num1
            menor = num2    
        if num3 < menor:    # num3 < num1
            menor = num3
        
        # Contar cuántas veces aparece el menor
        conteo = [num1, num2, num3].count(menor)
        
        if conteo == 1:
            print(f"El número menor es {menor} y es único.")
        else:
            print(f"El número menor es {menor} y se repite {conteo} veces.")
    
    except ValueError:
        print("Error: Por favor ingresa solo números enteros.")

# Ejecutar el programa
encontrar_menor()