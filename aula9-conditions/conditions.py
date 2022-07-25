"""
Condições IF, ELIF (else if) e ELSE
"""
a = True
if a:
    print("Verdadeiro.")

if not a:
    print("Olá")
# Olá não foi impresso


if True:
    print("True2")
else:
    print("Não será impresso")

if False:
    print("Não será impresso")
elif True:
    print("True3")
else:
    print("Não será impresso")

