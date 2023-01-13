# Escreva um programa que faça o compudar "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
# o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numberRandom = random.randrange(1, 5) # Valor gerado aleatóriamente pelo computador
userChoose = int(input('Digite um número entre [0 - 5] e tente adivinhar o valor gerado aleatóriamente: ')) # Valor escolhido pelo jogador
if numberRandom == userChoose:
    print('O número aleatório gerado foi {:.0f}, parabéns, você acertou'.format(numberRandom))
else:
    print('O número gerado aleatóriamente foi {:.0f}, infelizmente você errou'.format(numberRandom))