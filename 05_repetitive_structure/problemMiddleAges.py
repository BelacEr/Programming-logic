def ingresar_numero(mensaje):
    while True:
        try:
            valor = input(mensaje)
            if valor == '':
                return None  # Uso de None para indicar fin de entrada
            valor_float = float(valor)
            if valor_float < 0:
                print("Error: La edad no puede ser negativa.")
                continue
            return valor_float
        except ValueError:
            print("Error: Por favor ingresa solo números válidos.")

def calcular_media(lista_edades):
    if not lista_edades:  # Verificar si la lista está vacía
        print("No se ingresaron edades para calcular la media.")
        return
    
    suma = sum(lista_edades)  # Suma de todos los números
    promedio = suma / len(lista_edades)
    print(f"MEDIA: {promedio:.2f}")  # Formateamos a 2 decimales

def main():
    edades = []
    print("Ingrese las edades (deje vacío para terminar):")
    while True:
        edad = ingresar_numero('Edad: ')
        if edad is None:  # Verificamos si el usuario terminó la entrada
            break
        edades.append(edad)
    
    calcular_media(edades)

if __name__ == "__main__":
    main()