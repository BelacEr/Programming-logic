def ingresar_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número válido.")

def main():
    x = ingresar_numero('Ingresar primer número: ')
    y = ingresar_numero('Ingresar segundo número: ')

    menor = min(x, y)  # Obtenemos el menor de los dos
    mayor = max(x, y)  # Obtenemos el mayor de los dos

    suma = 0
    # Iteramos desde menor+1 hasta mayor-1 para excluir los extremos
    for num in range(menor + 1, mayor):
        if num % 2 != 0:  # Verificamos si es impar
            suma += num
    
    print(f"SUMA DE NÚMEROS IMPARES= {suma}")

main()