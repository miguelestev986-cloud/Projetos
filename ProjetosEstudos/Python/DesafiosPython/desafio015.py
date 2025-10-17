print('''Aula 1.7
Aluguel de Carros
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que 
o carro custa R$60 por dia e R$0,15 por Km rodado.
''')
d= int(input('Quantos dias alugados? '))
km= float(input('Quantos Km rodados? '))
total= 60 * d + 0.15 * km
print(f'O total a ser pago é R${total:.2f}')
