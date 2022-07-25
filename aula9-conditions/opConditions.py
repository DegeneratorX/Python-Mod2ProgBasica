"""
Operadoress

== igualdade
>= maior ou igual
> maior que
< menor que
<= menor ou igual
!= diferente

"""

print(2 == 2)  # Retornará True

print(2 == 1)  # Retornará False

print(2 == '2')  # Retornará False, pois String != Int

########################################

num_1 = 2  # int
num_2 = 2  # int

expressao = (num_1 == num_2)  # O operador == pergunta se é verdadeiro ou falso e atribui a "expressao"

print(expressao)  # True

expressao = (num_1 > num_2)

print(expressao)  # False

##########################################

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

# Limite para pegar empréstimo
idade_menor = 20
idade_maior = 80

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')

