def ingresar_notas(notas):
    while True:
        try:
            return float(input(notas))
        except ValueError:
            print("Entrada fallida. Por favor, asegúrate de solo ingresar números.")

notas = []
notas.append(ingresar_notas('Introduzca la primera nota: '))
notas.append(ingresar_notas('Introduzca la segunda nota: '))

nota_final = (notas[0] + notas[1])
if nota_final < 60.00:
    print(f"Nota final {nota_final:.1f}")
    print('SUSPENDIDO')
else:
    print(f"Nota final {nota_final:.1f}")
