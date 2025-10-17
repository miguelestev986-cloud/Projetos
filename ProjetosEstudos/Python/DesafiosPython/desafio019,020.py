print('Aula 1.8 - Utilizando módulos')
from random import choice,shuffle
print('Desafio 19')
aluno1= input('Digite o nome do primeiro aluno: ')
aluno2= input('Digite o nome do segundo aluno: ')
aluno3= input('Digite o nome do terceiro aluno: ')
aluno4= input('Digite o nome do quarto aluno: ')
lista_alunos= [aluno1, aluno2, aluno3, aluno4]
print(f'O estudante sorteado é {choice(lista_alunos)}')
print('\nDesafio 20')
shuffle(lista_alunos)
print(f'''
O primeiro a apresentar é {lista_alunos[0]}
O segundo a apresentar é {lista_alunos[1]}
O terceiro a apresentar é {lista_alunos[2]}
O quarto a apresentar é {lista_alunos[3]}''')
