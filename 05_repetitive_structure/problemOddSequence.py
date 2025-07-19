import sys

def ingresar_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print('\nBye!')
            sys.exit()

def odd_sequence():
    x = ingresar_numero('Introduzca el valor de x: ')
        
    for num in range(1, x + 1):
        if num % 2 != 0:   
            print(num)

# ejecutar programa
odd_sequence()