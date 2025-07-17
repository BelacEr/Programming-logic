def ingresar_numero(datos):
    while True:
        try:
            return float(input(datos))
        except ValueError:
            print("Error: Debes ingresar un número válido. Inténtalo de nuevo.")

def temperatura():
    escala = input('¿En qué escala (C/F) vas a introducir la temperatura? ')
    if escala == 'F':
        fahrenheit = ingresar_numero('Introduzca la temperatura en Fahrenheit: ')
        equivalencia_C = (fahrenheit - 32) * 5/9    # C = (F - 32) * 5/9
        print(f"Temperatura equivalente en grados Celsius: {equivalencia_C:.2f}")
    elif escala == 'C':
        celsius = ingresar_numero('Introduzca la temperatura en Celsius: ')
        equivalencia_F = (celsius * 9/5) + 32                  #F = (C * 9/5) + 32
        print(f"Temperatura equivalente en Fahrenheit: {equivalencia_F:.2f}")
    else:
        print('Asegúrate de escribir solo F o C en mayúsculas.')
        
# Ejecutar el programa -w-
temperatura()