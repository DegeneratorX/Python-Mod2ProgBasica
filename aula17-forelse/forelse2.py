"""For/Else em python"""

variavel = ['Luiz Otávio', 'Carlos', 'Maria']

# Existe uma forma mais otimizada de escrever o código do arquivo anterior.

for valor in variavel:
    print(valor)
    if valor.lower().startswith('j'):
        break
else:  # Se percorrer o laço e não tiver interrupção, ele dá um else.
    print('Não existe uma palavra que começa com J.')

# Não é muito utilizado, mas fica de conhecimento.
