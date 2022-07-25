"""
Listas
fatiamento [começo:até quanto:passos]
append, insert, pop, del, clear, extend, +
min, max
range
"""

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2

print(l1)
print(l2)
print(l3)  # Imprimirá [1,2,3,4,5,6]. É uma forma de juntar listas, mas não é a melhor.

####################################
print("###################################")

# .extend(x) - insere uma lista dentro de outra.

l1.extend(l2)  # mesmo resultado de l3
print(l1)
l1.extend('a')  # "adiciona" 'a' a lista. O problema é que a função extend não é adequada para adição, e sim pra juntar.
print(l1)

####################################
print("###################################")

l1.append('b')  # adiciona b ao final da lista de forma apropriada.
print(l1)
print(l1[7])  # agora tem 8 índices, sendo o índice 7 o valor b.

####################################
print("###################################")

l2.insert(1, 'banana')  # o insert adiciona em qualquer lugar da lista. Recebe o valor do índice pra adicionar. O resto
#                         é empurrado pra frente.
print(l2)
print(l2[1])

####################################
print("###################################")

l2.pop()  # o pop retira o último elemento da lista.
print(l2)

####################################
print("###################################")

#     0 1 2 3 4 5 6 7 8
l4 = [1,2,3,4,5,6,7,8,9]

del(l4[3:5])  # excluirá entre 3 e 6. Esse é o intervalo.
print(l4)

####################################
print("###################################")

l5 = [91,23,56,38,43,37]

print(max(l5))  # Maior valor da lista (inteiro)
print(min(l5))  # Menor valor da lista (inteiro)

####################################
print("###################################")

l6 = range(1,10)  # Função range() do laço for. Percorre 1 até 9.
print(l6)  # Normalmente não acontece nada. Ele simplesmente printa a função.

l6 = list(range(1,10))  # Mas se eu adicionar a função list a função iterável range, eu converto pra lista.
print(l6)  # E com isso não precisa digitar 123...89 dentro de uma lista.


