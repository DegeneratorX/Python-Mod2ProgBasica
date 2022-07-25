"""For/Else em python"""

variavel = ['Luiz Otávio', 'João', 'Maria']

for valor in variavel:
    if valor.startswith('J'):  # Função que verifica se a string começa com certa letra.
        print(f"Essa palavra {valor} começa com J.")
    else:
        print(f"Essa palavra {valor} não começa com J.")

#######################################
startwith_m = False

for valor in variavel:
    if valor.lower().startswith("m"):  # .lower() diminui todas as letras da palavra, assim não precisando diferenciar
        #                                maiúsculas de minúsculas na hora da iteração.
        startwith_m = True

if startwith_m:
    print("Existe uma palavra que começa com M.")
else:
    print("Não existe uma palavra que começa com M.")
