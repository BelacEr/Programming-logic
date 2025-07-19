def ingresar_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número válido.")

def main(valor):
    # función que determina si el valor es par o impar (el 0 es para terminar el algoritmo)
    if valor == 0:  # condición para terminar el programa
        return None
    
    if valor % 2 == 0:  # si el número es par
        suma = 0
        for num in range(5):
            nuevo_valor = valor + 2 * num
            suma += nuevo_valor
    else:               # si el número es impar
        suma = 0
        valor += 1
        for num in range(5):
            nuevo_valor = valor + 2 * num
            suma += nuevo_valor
    
    return suma  # Faltaba retornar la suma

while True:
    entero = ingresar_numero('Introduzca un número entero (0 para salir): ')
    if entero == 0:
        print("Programa terminado.")
        break
    
    suma_total = main(entero)
    print(f"La suma es: {suma_total}")
