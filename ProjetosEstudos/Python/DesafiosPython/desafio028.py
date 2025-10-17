from random import randint
num = int(randint(0,5))
print('-=-'*10)
respuesta = int(input('Adivina un número del 0 al 5: '))
print('-=-'*10)
if respuesta == num:
    print('\nFelicidades, ganaste')
else:
    print(f'\nPerdiste, el número era {num} y no {respuesta}!')
