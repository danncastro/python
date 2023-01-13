# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nomePessoa = input('Digite um nome: ').strip()

print('Esse nome pessoa contém SILVA?? {}'.format('Silva' in nomePessoa.title()))