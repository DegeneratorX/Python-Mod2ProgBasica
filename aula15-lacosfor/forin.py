"""
For in
Iterando Strings com for
Função range(start=0, stop, step=1), onde start é o começo, stop é onde parar e step é as casas que pula.
"""

texto = 'Python'

for letra in texto:  # Cria uma variável local "letra" pro for e checa dentro da variável "texto"
    print(letra)  # Imprime toda a palavra Python.

print("")
###########################

for numero in range(10):  # Por padrão essa função é lida assim: range(0,10,1)
    print(numero)  # Imprimirá de 0 a 9.

print("")

for numero in range(3, 10, 2):  # contador começa no 3, termina no 10 e pula 2 casas.
    print(numero)
