# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
# Exemplo: 
# Digite um número: 6.127
# O número 6.127 tem a parte inteira 6

from math import floor
numeroReal = float(input('Digite um valor: '))

#Utilizando modulos importados
print('O valor digitado foi {} a porção inteira desse valor é {}'.format(numeroReal, floor(numeroReal)))

# Utilizando funções internas do Python
print('O valor digitado foi {} a porção inteira desse valor é {}'.format(numeroReal, int(numeroReal)))
