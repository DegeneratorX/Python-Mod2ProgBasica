"""
Enumerate - Enumerar elementos da lista
"""

lista = [
    # 0       1        2
    ['Edu', 'João', 'Luiz'],  #     0
    ['Maria', 'Aline', 'Joana'],  # 1
    ['Helena', 'Ed', 'Lu']  #       2
]

print(lista[1][2])  # Busca a palavra Joana

for v1, v2 in enumerate(lista):
    print(v1,v2)