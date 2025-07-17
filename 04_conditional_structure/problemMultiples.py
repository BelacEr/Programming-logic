def ingresar_numeros(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: El valor no puede ser negativo. Inténtalo de nuevo.")
                continue
            return valor
        except ValueError:
            print("Error: Por favor ingresa solo números enteros.")

def son_multiplos(num1, num2):
    # Verificar si uno es múltiplo del otro 
    if num1 == 0 or num2 == 0:
        print("Advertencia: Uno de los números es cero. Cero solo es múltiplo de sí mismo.")
        return False
    
    if num1 % num2 == 0 or num2 % num1 == 0:
        print('Son múltiplos.')
        return True
    else:
        print('No son múltiplos.')
        return False

print('Introduzca dos números enteros:')
print('--------------------------------')
num1 = ingresar_numeros('Ingrese el primer número: ')   
num2 = ingresar_numeros('Ingrese el segundo número: ')

son_multiplos(num1, num2)