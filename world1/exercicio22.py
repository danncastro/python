# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas.
# Quantas letras ao todo (Sem considerar espaços)
# Quantas letras tem o primeiro nome

nomePessoa = input('Digite um nome: ')
print()

print('Letras maiúsculas \n{}'.format(nomePessoa.upper()))
print()

print('Letras minúsculas \n{}'.format(nomePessoa.lower()))
print()

print('Quantidade de letras ao todo sem espaços \n{}'.format(len(nomePessoa) - nomePessoa.count(' ')))
print()

print('Quantidade de letras no primeiro nome')
primeiroNome = nomePessoa.split()
print(len(primeiroNome[0]))
print()