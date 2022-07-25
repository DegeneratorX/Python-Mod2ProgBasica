"""
str - string
"""

print('Essa é uma string')  # string, as aspas.
print("Também é, mas em aspas duplas")  # também pode usar duplas
print(123456)  # não é string, o python detecta isso

# tudo que estiver em aspas, é ‘string’, incluindo a documentação de aspas tripla.

print("Essa é uma 'string' (str)")  # Colocar aspas simples dentro de uma dupla funciona.
# Colocar uma simples dentro de outra simples não funciona. Por isso existem dois tipos de aspas para string.

print(r'Esse é meu \n texto (str)')  # colocar "r" antes da string avisa ao compilador que tudo que estiver dentro,
# não pode ser executado como código, por exemplo, \n, que significa quebra de linha.
