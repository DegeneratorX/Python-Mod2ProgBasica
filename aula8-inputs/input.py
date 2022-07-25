"""
Entrada de dados
"""

nome = input("Qual o seu nome? ")  # atribui um valor de input nessa variavel nome.
print(f'O usuário digitou {nome} e o tipo da variável é {type(nome)}')

# Sempre nesse caso será str,a mesmo digitando 10, será reconhecido como string.

idade = input("Qual a sua idade? ")



# Pra usar inteiro da string do input da idade, é necessário converter a string em int.

ano_nascimento = 2022-int(idade)  # Assim posso fazer a subtração

print(f'{nome} tem {idade} anos.'
      f'{nome} nasceu em {ano_nascimento}.')


