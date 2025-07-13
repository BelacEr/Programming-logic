data = []
print('Datos de la primera persona: ')
name = input('Nombre: ')
while True:
    try:   
        data.append(int(input('Edad (años): ')))
        break
    except ValueError:
        print('Entrada fallida. Por favor, asegurate de solo ingresar números.')
print('Datos de la segunda persona: ')
name_2 = input('Nombre: ')
while True:
    try:
        data.append(int(input('Edad: ')))
        break
    except ValueError:
        print('Entrada fallida. Por favor, asegurate de solo ingresar números.')

print('La edad media de ' + name + ' y ' + name_2 + ' es de ' + str(data[0] + data [1] / len(data)))

