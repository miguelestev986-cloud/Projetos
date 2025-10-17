frase = input('Ingresa una frase: ').upper().strip()
print(f'''La letra "A" aparece {frase.count('A')} veces.
La letra "A" aparece la primera vez en el caracter {frase.find("A")}
La letra "A" aparece la ultima vez en el caracter {frase.rfind("A")}''')
