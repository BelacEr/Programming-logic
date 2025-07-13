import math 

print('Base del rectángulo: ')
base = float(input())
print('Altura del rectángulo:')
altura = float(input())
print('Área: ' + str(base*altura))
print('Perímetro ' + str(2 * base + 2 * altura))
print('Diagonal ' + str(math.sqrt((altura ** 2 + base ** 2))))
