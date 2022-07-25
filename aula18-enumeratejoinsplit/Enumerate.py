"""
Split, Join, Enumerate
Split - Dividir uma string # str
Join - Juntar uma lista # str
Enumerate - Enumerar elementos da lista # iteráveis
"""

string = 'O Brasil é penta.'
lista = string.split(' ')  # Separa a string em uma lista

for indice, valor in enumerate(lista):  # indice = 0,1,2... valor = valor dentro da lista.
    print(indice, valor, lista[indice])  # valor e lista[indice] são exatamente iguais. Enumerate é uma alternativa.
