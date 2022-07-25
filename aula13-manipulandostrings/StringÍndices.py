"""
Manipulando Strings

-String íncides
-Fatiamento de strings [inicio:fim:passo]
-Funções built-in len, abs, type, print etc...
"""

# positivos    [012345678]   <--- Índices de cada letra da string abaixo.
texto        = 'Python s2'
# negativos   -[987654321]

print(texto[2])  # índice 2. Aparecerá a letra 't', pois o índice é 2, como mostrado acima.

nova_string = texto[2:6]  # começa do 2 e termina no 6. Irá imprimir "thon"
print(nova_string)
nova_string = texto[:6]
print(nova_string)

##########

nova_string = texto[-9:-3]  # Imprimirá python.
print(nova_string)
