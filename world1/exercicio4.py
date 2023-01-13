# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

mensagem = input('Digite alguma informação: ')

print('Valida seu tipo primitivo: ', type(mensagem))
print('Valida se tem apenas espaços: ', mensagem.isspace())
print('Valida se o valor é um número: ', mensagem.isnumeric())
print('Valida se é um valor alfabético: ', mensagem.isalpha())
print('Valida se é um valor alfanúmerico : ', mensagem.isalnum())
print('Valida se o valor está em letras maiúsculas: ', mensagem.isupper())
print('Valida se o valor está em letras minúsculas: ', mensagem.islower())
print('Valida se o valor está captalizado: ', mensagem.istitle())