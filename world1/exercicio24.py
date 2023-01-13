# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

nomeCidade = input('Digite o nome da cidade: ').strip()

print('Essa cidade começa com SANTO? "{}"'.format(nomeCidade[:5].title() == 'Santo'))