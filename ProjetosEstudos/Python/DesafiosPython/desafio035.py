pl = float(input('Ingresa la longitud del primer lado: '))
sl = float(input('Ingresa la longitud del segundo lado: '))
tl = float(input('Ingresa la longitud del tercer lado: '))
if pl + sl > tl and pl + tl > sl and sl + tl > pl:
    print('Ellos pueden formar un triangulo')
else:
    print('Ellos no pueden formar un triangulo')
