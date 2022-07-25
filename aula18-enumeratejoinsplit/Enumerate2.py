lista = [[0, 'Victor'], [1, 'João'], [2, 'Maria']]

# É possível criar listas dentro de uma lista.

for indice, nome in lista:  # Crio duas variáveis Indice e Nome e percorro a lista. Isso se chama desempacotar.
    print(indice, nome)  # Se colocar um terceiro valor em qualquer das listas acima, ocorrerá um erro.
# Tudo funciona de forma automática.
######################################
print()

lista2 = ['Victor', 'João', 'Maria']

for indice, nome in enumerate(lista):  # Isso faz exatamente o que está em cima.
    print(indice, nome)

#######################################
print()
# Outra forma de desempacotar:

n1,n2,n3 = lista2

print(n1,n2,n3)
