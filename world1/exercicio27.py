# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# Ex:
# Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nomePessoa = input('Digite seu nome: ')
print()

nomeSegmentado = nomePessoa.split()
print('{}'.format(nomePessoa))
print()
print('Primeiro nome = {} \nÚltimo nome = {}'.format(nomeSegmentado[0], nomeSegmentado[-1]))