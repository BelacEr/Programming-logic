def obtener_segundos_validos():
    while True:
        try:
            segundos = int(input("Introduzca la duración en segundos: "))
            if segundos >= 0:
                return segundos
            print("¡Error! Ingrese un número entero no negativo.")
        except ValueError:
            print("¡Error! Ingrese un valor numérico válido.")

def convertir_a_formato_hms(segundos_totales):
    horas = segundos_totales // 3600
    segundos_restantes = segundos_totales % 3600
    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60
    return horas, minutos, segundos

def mostrar_tiempo_formateado(horas, minutos, segundos):
    print(f"{horas}:{minutos}:{segundos}")

# Flujo principal
if __name__ == "__main__":
    segundos_totales = obtener_segundos_validos()
    horas, minutos, segundos = convertir_a_formato_hms(segundos_totales)
    mostrar_tiempo_formateado(horas, minutos, segundos)