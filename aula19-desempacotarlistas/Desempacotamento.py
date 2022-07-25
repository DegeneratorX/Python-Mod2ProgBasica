"""
Desempacotamento de listas
"""
lista = ['Luiz', 'João', 'Maria']

n1, n2, n3 = lista  # Desempacotamento

print(n2)

#########################################

lista2 = ['Luiz', 'João', 'Maria', 'Generico', 1, 2, 3, 4, 8]

b1, b2, b3, *b4 = lista2  # O asterisco gera outra lista ao desempacotar.

print(b1, b2, b3, b4)

#########################################

c1, c2, c3, *c4, c5 = lista2

print(c1,c2,c3,c4,c5)  # Tudo após o asterisco serão os últimos números.
