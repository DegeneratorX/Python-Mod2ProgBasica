"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Ponto Flutuante (float)
:.(NÚMERO)F - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO -s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print(f"Resultado da divisão: {divisao:.2f}")

###########################

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0>10}')

print(f'{num_2:0^10}')

Titulo = "BeM viNdO"

print(f'{Titulo:=^20}')

print(f'{num_2:0^10.2f}')

print(Titulo.lower())  # Deixa tudo minúsculo
print(Titulo.upper())  # Deixa tudo maiúsculo
print(Titulo.title())  # Primeiras letras maiúsculas
