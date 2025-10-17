print('Aula 1.7\nCalculadora de tinta')
l=float(input('Largura da parede:'))
a=float(input('Altura da parede:'))
area=l*a
print('A área da parede {}m por {}m é {:.2f}m'.format(l, a, area))
print('A quantidade de tinta necessária será de {}l'.format(area/2))
