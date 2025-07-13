# Input
print('Introduzca la anchura de la parcela:')
anch = float(input())
print('Introduzca la longitud de la parcela:')
long = float(input())
print('Introduzca el valor del metro cuadrado:')
valor_m2 = float(input())


# Operation
print('Superficie de la parcela: ' + str(anch * long))
print('Precio del terreno: ' + str(anch * long * valor_m2))
