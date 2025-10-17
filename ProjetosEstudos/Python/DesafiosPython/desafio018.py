print('Aula 1.8 - Utilizando módulos')
from math import sin, cos, tan, radians
an = float(input('Digite el angulo que deseas: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print(f'''El angulo de {an} tiene el seno de {seno:.3f}
El cosseno de {cosseno:.3f}
Y la tangente de {tangente:.3f}''')
