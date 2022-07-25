string = "O Brasil é o país do futebol, o Brasil é penta."

lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_2:
    print(valor.strip().capitalize())
    # A função strip remove os espaços no começo e fim da string. Capitalize coloca maiúscula a primeira letra da frase.
