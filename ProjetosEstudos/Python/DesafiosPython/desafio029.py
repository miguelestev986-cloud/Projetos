v = int(input('Ingresa la velocidad del coche: '))
if v > 80:
    print(f'Fuiste multado en R${(v-80)*7}')
else:
    print('Tenga un buen día y conduzca con seguridad')