print('Aula 1.6\nCalculadora e "Prazer em te conhecer" ')
nome=input('Qual seu nome?')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome))
# faz com que o nome apareça em 20 caracteres
print('Prazer em te conhecer {:>20}!'.format(nome))
#alinha à direita
print('Prazer em te conhecer {:^20}!'.format(nome))
#centraliza
print(f'Prazer em te conhecer {nome:=^20}!')
n1=float(input('Digite um valor:'))
n2=float(input('Digite outro valor:'))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print(f'A soma é {s}\nO produto é {m}\nE a divisão é {d:.3}', end=' ,')
# {:.3} faz com que apareça em 3 casas decimais, \n quebra a linha e end='' não quebra a linha
print('a divisão inteira é {} e a potência é {}'.format(di, e))
