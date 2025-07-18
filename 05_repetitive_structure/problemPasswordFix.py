while True:
    password = '2312'
    intento = input('Introduzca la contraseña: ')
    if intento != password:
        while True:
            nuevo_intento = input('¡Contraseña inválida! Inténtelo de nuevo: ')
            if nuevo_intento != password:
                continue
            else:
                break   
        print('¡Acceso permitido!')
        break