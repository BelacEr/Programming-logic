def ingresar_numeros(datos): # Funcion para comprobar que en horas sean solo numeros.
    while True:
        try:
            return float(input(datos))
        except ValueError:
            print("Entrada fallida. Por favor, asegúrate de solo ingresar números.")

datos = []

nombre = input('Nombre: ')
datos.append(ingresar_numeros('Salario por hora: '))
datos.append(ingresar_numeros('Horas trabajadas: '))
paga = datos[0] * datos[1]
print(f"La paga de {nombre} debe ser de {paga:.2f}")
