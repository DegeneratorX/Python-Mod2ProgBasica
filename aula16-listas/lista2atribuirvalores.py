"""
Listas
fatiamento [começo:até quanto:passos]
append, insert, pop, del, clear, etend, +
min, max
range
"""

#         0    1    2    3    4     5
lista = ["A", "B", "C", "D", "E", 10.5]
lista[5] = "Qualquer coisa"  # Substitui o índice 5, que contém o float 10.5, e guarda essa string.

print(lista[5])
print(lista[0:3:])  # Será exibido 0, 1 e 2. Não inclui o 3.
print(lista[::2])  # Pula de 2 em 2
