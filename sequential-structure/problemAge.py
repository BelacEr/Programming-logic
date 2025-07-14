def ingresar_edad(ages):
    while True:
        try:
            return int(input(ages))
        except ValueError:
            print("Entrada fallida. Por favor, asegúrate de solo ingresar números.")


ages = []
print('Datos de la primera persona: ')
name = input('Nombre: ')
ages.append(ingresar_edad('Edad (años): '))

print('Datos de la segunda persona: ')
name_2 = input('Nombre: ')
ages.append(ingresar_edad('Edad (años): '))

print(f"La edad media de {name} y {name_2} es de {str((ages[0] + ages[1]) / len(ages))} años.")

