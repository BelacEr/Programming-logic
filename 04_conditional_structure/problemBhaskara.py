import math

def ingresar_numeros(datos):
    while True:
        try:
            return float(input(datos))
        except ValueError:
            print("¡Error! Debes ingresar un número válido. Inténtalo de nuevo.")

print("Resolución de ecuaciones cuadráticas (ax² + bx + c = 0)")
a = ingresar_numeros('Ingresar el coeficiente a: ')
b = ingresar_numeros('Ingresar el coeficiente b: ')
c = ingresar_numeros('Ingresar el coeficiente c: ')


if a == 0:
    print("No es una ecuación cuadrática (a debe ser ≠ 0).")
else:
    discriminante = b ** 2 - 4 * a * c  
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        print(f"Raíces reales: x1 = {x1:.4f}, x2 = {x2:.4f}")
    elif discriminante == 0:
        x = -b / (2 * a)
        print(f"RRaíz doble:: {x:.4f}")
    else:
        print('La ecuación no tiene soluciones reales. En este caso, las soluciones son números complejos.')


