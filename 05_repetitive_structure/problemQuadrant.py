def leer_coordenada(mensaje):
    while True:
        valor = input(mensaje)
        if valor == "":  # NULL (input vacío)
            return None
        try:
            return float(valor)
        except ValueError:
            print("Error: Ingresa un número válido o deja vacío para terminar.")

def determinar_cuadrante(x, y):
    if x > 0 and y > 0:
        return "Q1"
    elif x < 0 and y > 0:
        return "Q2"
    elif x < 0 and y < 0:
        return "Q3"
    elif x > 0 and y < 0:
        return "Q4"
    else:
        return None  # Está en un eje o en el origen (no es un cuadrante)

while True:

    print("Introduzca los valores de las coordenadas X e Y:")
    
    x = leer_coordenada("X: ")
    if x is None:  # Termina si X es NULL
        break
    
    y = leer_coordenada("Y: ")
    if y is None:  # Termina si Y es NULL
        break
    
    cuadrante = determinar_cuadrante(x, y)
    if cuadrante:
        print(f"CUADRANTE {cuadrante}")
    # Si no hay cuadrante (ejes/origen), no imprime nada y continúa