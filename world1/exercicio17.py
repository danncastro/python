# Faça um programa que leia o comprimento do cateto oposto de um triângulo e do cateto adjacente de um triângulo retângulo
# calcule e mostre o comprimento da hipotenusa.

from math import hypot

catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)

# Método utilizando funções internas
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

# Método importando bibliotecas
hypot(catetoOposto, catetoAdjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))