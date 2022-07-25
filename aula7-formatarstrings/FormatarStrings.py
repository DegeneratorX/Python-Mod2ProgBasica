nome: str = 'Victor'
idade = 25
altura: float = 1.85
e_maior = idade > 18  # se idade for maior que 18, retorna true
peso = 110
imc = peso / (altura ** 2)
ano_atual = 2022
data_nascimento = ano_atual-idade

print(nome, 'tem', idade, 'anos de idade,', 'possui', altura, 'de altura,', 'pesa', peso, 'kg', 'e tem IMC', imc)

print(f'{nome} tem {idade} anos de idade, possui {altura} de altura, pesa {peso}kg e tem imc {imc:.2f}')

""" Quando quiser formatar, basta colocar o "f" antes da string dentro da função print. Fica semelhante a como se
utiliza em C e C++. De quebra, é possível ajustar as casas decimais em números float, ao colocar, por exemplo,
":.2f", que significa que só vai exibir 2 casas decimais."""

print('{} tem {} anos de idade, possui {} de altura, pesa {}kg e tem imc {:.2f}'.format(nome, idade, altura, peso, imc))
print('{0} tem {1} anos de idade, possui {2} de altura, pesa {3}kg e tem imc {4:.2f}'.format(nome, idade, altura, peso,
                                                                                             imc))

"""Esse formato é diferenciado pois ele numera de 0 a 4 (deixando em branco ele automaticamente põe de 0 a 4 por trás
do compilador) e você tem a opção de ordenar da forma que quiser. Se ficar 4,3,2,1,0, os valores serão exibidos de
forma contrária."""

print(
    '{n} tem {i} anos de idade, possui {h} de altura, pesa {p}kg e tem imc {imc:.2f}.'.format(n=nome, i=idade, h=altura,
                                                                                             p=peso, imc=imc), end='')

"""Também dá pra atribuir dentro da print letras e no final designar o que cada uma significa. Além de claro, usar o
end='' para a print não pular uma linha pro próximo comando."""

print(f' {nome} nasceu em {data_nascimento}')
