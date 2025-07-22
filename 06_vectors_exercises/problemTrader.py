def ingresar_numero(mensaje, tipo='float'):
    while True:
        try:
            entrada = input(mensaje)
            if tipo == 'int':
                return int(entrada)
            return float(entrada)
        except ValueError:
            print("Error: Ingresa un número válido.")

def clasificar_beneficio(compra, venta):
    porcentaje = ((venta - compra) / compra) * 100

    if porcentaje < 10:
        return 1, 0, 0
    elif 10 <= porcentaje <= 20:
        return 0, 1, 0
    else:
        return 0, 0, 1

def main():
    N = ingresar_numero('¿Cuántos productos se introducirán? ', tipo='int')
    total_compra = 0
    total_venta = 0
    beneficio_10 = 0
    beneficio_10_20 = 0
    beneficio_20 = 0
    beneficio_total = 0

    for i in range(N):
        print(f"\nProducto {i + 1}:")
        input('Nombre: ')  # Se pide el nombre, pero no se usa
        precio_compra = ingresar_numero('Precio de compra: ')
        precio_venta = ingresar_numero('Precio de venta: ')

        beneficio_total += (precio_venta - precio_compra)
        total_compra += precio_compra
        total_venta += precio_venta

        menos10, entre10y20, mas20 = clasificar_beneficio(precio_compra, precio_venta)
        beneficio_10 += menos10
        beneficio_10_20 += entre10y20
        beneficio_20 += mas20

    # Resultado
    print('\n' + 'INFORME'.center(36, '='))
    print(f"Beneficio inferior al 10%: {beneficio_10}")
    print(f"Beneficio entre 10% y 20%: {beneficio_10_20}")
    print(f"Beneficio superior al 20%: {beneficio_20}")
    print(f"Valor total de la compra: {total_compra:.2f}")
    print(f"Valor total de la venta: {total_venta:.2f}")
    print(f"Beneficio total: {beneficio_total:.2f}")

if __name__ == '__main__':
    main()