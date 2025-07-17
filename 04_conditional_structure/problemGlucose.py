def ingresar_numeros(datos):    # Comprobar que los datos ingresados sean números
    while True:
        try:
            valor = float(input(datos))
            if valor < 0:
                print("Error: El valor no puede ser negativo. Inténtalo de nuevo.")
                continue
            return valor
        except ValueError:
            print("Error: Debes ingresar un número válido. Inténtalo de nuevo.")
  
def clasificar_glucosa(nivel):  # Clasificación de la glucosa
    if nivel < 70:
        return " Clasificación: Baja"
    elif 70 <= nivel <= 100:
        return " Clasificación: Normal"
    elif 100 < nivel <= 140:
        return " Clasificación: Alta"
    else:
        return " Clasificación: Diabetes"

# Programa principal
print("Clasificación de Niveles de Glucosa")
print("-----------------------------------")

nivel_glucosa = ingresar_numeros("Introduzca su medición de glucosa (mg/dL): ")
clasificacion = clasificar_glucosa(nivel_glucosa)

print(f"\nResultado: {clasificacion}")
print(f"Valor ingresado: {nivel_glucosa} mg/dL")