s = float(input('Ingresa el valor del salario: R$'))
if s > 1250:
    print(f'El salario con aumento es de R${s+(s*0.10)}')
else:
    print(f'El salario con aumento es de R${s+(s*0.15)}')
