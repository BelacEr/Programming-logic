def ingresar_numeros(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Error: El valor no puede ser negativo. Inténtalo de nuevo.")
                continue
            return valor
        except ValueError:
            print("Error: Por favor ingresa solo números.")

def salario_aumento(salario):
    if salario <= 1000.00:
        porcentaje = 20
        aumento = salario * 0.20 
        nuevo_salario = salario + aumento       # aumento del 20%
    elif 1000.00 < salario <= 3000.00:
        porcentaje = 15
        aumento = salario * 0.15 
        nuevo_salario = salario + aumento       # aumento del 15%
    elif 3000.00 < salario <= 8000.00:
        porcentaje = 10
        aumento = salario * 0.10
        nuevo_salario = salario + aumento       # aumento del 10%
    else:
        porcentaje = 5
        aumento = salario * 0.5 
        nuevo_salario = salario + aumento       # aumento del 5%    
    
    print(f"Nuevo salario: R$ {nuevo_salario:.2f}")
    print(f"Aumento: R$ {aumento:.2f}. Porcentaje: {porcentaje}%")

salario = ingresar_numeros('Introduzca el salario de la persona: ')  
salario_aumento(salario)