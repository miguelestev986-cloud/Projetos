print('Aula 1.8 - Utilizando módulos')
import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = math.hypot(co, ca)
print(f'A hipotenusa vale {h}.')