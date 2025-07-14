def ingresar_numero(datos):
    while True:
        try:
            return float(input(datos))
        except ValueError:
            print("Entrada fallida. Por favor, asegúrate de solo ingresar números.")

datos = []
datos.append(ingresar_numero('Distancia recorrida (km): '))
datos.append(ingresar_numero('Combustible utilizado (km): '))
consumo = datos[0] / datos[1]

print(f"Consumo medio {consumo:.3f}")        