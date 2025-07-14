def ingresar_numeros(datos):
    while True:
        try:
            return float(input(datos))
        except ValueError:
            print("Entrada fallida. Por favor, asegúrate de solo ingresar números.")

datos = []
datos.append(ingresar_numeros('Ingresar medida A: '))
datos.append(ingresar_numeros('Ingresar medida B: '))
datos.append(ingresar_numeros('Ingresar medida C: '))

areas = []
areas.append(datos[0] ** 2)
areas.append(datos[0] * datos[1] / 2)
areas.append((datos[0] + datos[1]) * datos[2] / 2)
# Area del cuadrado A^2
# Area del triangulo A*B/2
# Area del triangulo trapecio (A * B) * C / 2


print(f"Área del cuadrado: {areas[0]:.4f}")
print(f"Área del triángulo: {areas[1]:.4f}")
print(f"Área del triángulo trapecio: {areas[2]:.4f}")