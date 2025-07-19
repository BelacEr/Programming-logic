import sys

def ingresar_numeros(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número válido.")

def tabla_multiplicar():
    numero = ingresar_numeros('¿Para qué valor quieres la tabla de multiplicar? ')
    for num in range(1, 11):
        total = numero * num
        print(f"{numero} x {num} = {total}")

# ejecutar programa
tabla_multiplicar()