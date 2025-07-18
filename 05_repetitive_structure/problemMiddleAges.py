def ingresar_numero(mensaje):
    while True:
        try:
            valor = input(mensaje)
            if valor == '':
                return valor
            return float(valor)
        except ValueError:
            print("Error: Por favor ingresa solo números.")

def media():
    # Función para obtener la media de la lista.
    suma = 0
    for i in range(len(edades)):    # suma de todos los números en la lista
        suma += + edades[i]

    promedio = suma / len(edades)
    print(f"MEDIA: {promedio}")


edades = []
while True:
    edades.append(ingresar_numero('Inserte edad: '))
    if edades[-1] == '':
        edades.remove('')
        break

media()