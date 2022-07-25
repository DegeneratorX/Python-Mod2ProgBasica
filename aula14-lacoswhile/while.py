"""
While
"""

x = 0
while x < 5:
    print(x)
    x += 1  # x = x + 1

print("Acabou!")

#################################
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue  # Tudo daqui pra baixo não será executado mais enquanto estiver dentro do While. Ele irá pro proximo
    # looping.
    print(x)
    x = x + 1

##################################
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break  # Força o python a sair do looping.
    print(x)
    x = x + 1
