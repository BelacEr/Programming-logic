def ingresar_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número válido.")

def clasificar_numero(numero):
    paridad = 'par' if numero % 2 == 0 else 'impar'

    if numero > 0: 
        signo = 'positivo'
    elif numero < 0:
        signo = 'negativo'
    else:
        signo = 'cero'

    return paridad, signo

def main():
    cantidad = ingresar_numero('¿Cuántos números vas a escribir? ')
    numero = 0

    for _ in range(cantidad):
        numero = ingresar_numero('Escriba un número: ')
        paridad, signo = clasificar_numero(numero)
        print(f"El número {numero} es: ")
        print(f"- {paridad.upper()}")
        print(f"- {signo.upper()}")

if __name__ == "__main__":
    main()

    

    
