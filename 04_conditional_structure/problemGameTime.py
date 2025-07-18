def ingresar_numeros(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: El valor no puede ser negativo. Inténtalo de nuevo.")
                continue
            return valor
        except ValueError:
            print("Error: Por favor ingresa solo números.")
            

inicio = ingresar_numeros('Hora de inicio: ')
final = ingresar_numeros('Hora de finalización: ')

if inicio < final:
    tiempo = final - inicio
else:
    tiempo = final + 24 - inicio

print(f"EL JUEGO DURÓ {tiempo} HORA(S).")