"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Victor'
idade = 25
altura = 1.85
e_maior = idade > 18  # se idade for maior que 18, retorna true
peso = 110

print(nome, type(nome))


print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É de maior:', e_maior)

print('IMC:', peso/(altura**2))

imc = peso/(altura**2)

print(nome, 'tem', idade, 'de idade,', 'possui', altura, 'de altura,', 'pesa', peso, 'kg', 'e tem IMC', imc)