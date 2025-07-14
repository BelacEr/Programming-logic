import math

while True:
    try:
        print('Introduzca el valor del radio del círculo:')
        radio = float(input())
        break
    except ValueError:
        print("Entrada fallida. Por favor, asegúrate de solo ingresar números.")


print(f"Área: {math.pi * radio**2:.3f}")
