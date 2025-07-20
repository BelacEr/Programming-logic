def ingresar_numero(mensaje, tipo='int'):
    while True:
        try:   
            entrada = input(mensaje)
            if tipo == 'str':
                return entrada
            return int(entrada)
        except ValueError:
            print(f"Error: Ingresa {'un número entero.' if tipo == 'int' else 'una letra válida.'}")

def informe(cobayas_dict): # (R:Rata S:Rana C:Conejo)
    total = sum(cobayas_dict.values())
    
    rata_porcent = cobayas_dict['rata'] * 100 / total
    rana_porcent = cobayas_dict['rana'] * 100 / total
    conejo_porcent = cobayas_dict['conejo'] * 100 / total
    
    print('INFORME FINAL'.center(36, '='))
    print(f"TOTAL: {total} cobayas.")
    print(f"Total ratas: {cobayas_dict['rata']}")  
    print(f"Total ranas: {cobayas_dict['rana']}")  
    print(f"Total conejos: {cobayas_dict['conejo']}")  
    
    print(f"\nPorcentaje de ratas: {rata_porcent:.2f}%")
    print(f"Porcentaje de ranas: {rana_porcent:.2f}%")
    print(f"Porcentaje de conejos: {conejo_porcent:.2f}%")

def main():
    cantidad = ingresar_numero('¿Cuántos casos de prueba se escribirán? ')
    cobayas = {'rata': 0, 'rana': 0, 'conejo': 0}

    for _ in range(cantidad):
        numero = ingresar_numero('Número de cobayas: ')
        tipo = ingresar_numero('Tipo de cobaya (R:Rata S:Rana C:Conejo): ', tipo='str')  

        if tipo.upper() == 'R':
            cobayas['rata'] += numero
        elif tipo.upper() == 'S':
            cobayas['rana'] += numero
        elif tipo.upper() == 'C':
            cobayas['conejo'] += numero
        else:
            print('Error: Tipo no válido. Use R, S o C.')

        print('-' * 30)

    informe(cobayas)

if __name__ == '__main__':
    main()