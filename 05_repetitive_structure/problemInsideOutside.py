def ingresar_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número válido.")

def clasificar_numeros(lista):
    # Clasifica los números en 'dentro' (10-20) y 'fuera' del rango.
    dentro = [num for num in lista if 10 <= num <= 20]
    fuera = [num for num in lista if num not in range(10, 21)]
    return dentro, fuera

def main():
    # Función principal que ejecuta el programa. 
    numeros = []
    cantidad = ingresar_numero('¿Cuántos números vas a escribir? ')

    for _ in range(cantidad):
        numeros.append(ingresar_numero('Escribe un número: '))
    
    dentro_rango, fuera_rango = clasificar_numeros(numeros)
    
    print("\nNúmeros dentro del rango [10, 20]:", dentro_rango)
    print("Números fuera del rango [10, 20]:", fuera_rango)

if __name__ == "__main__": # Ésto porque se ve cuqui
    main()