def ingresar_numero(mensaje):   
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print('Ingresa solo números naturales (positivos).')
                continue
            return valor
        except ValueError:
            print("Error: Ingresa un número válido.")

def factorial(n):
    # Calcula el factorial de n usando un bucle
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def main():
    numero = ingresar_numero("Introduzca el valor de N: ")
    resultado = factorial(numero)
    print(f"FACTORIAL: {resultado}")

if __name__ == '__main__':
    main()