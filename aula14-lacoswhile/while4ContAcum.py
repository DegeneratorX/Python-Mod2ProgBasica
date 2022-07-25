"""
While / Else
contadores
acumuladores
"""

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1

###############################

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:  # Esse else tem utilidade na seguinte situação: quando tem break no while, o else não é lido.
    print("Cheguei no else. Por conta do 'break', não serei executado.")
print("Mas isso aqui sim será executado.")
