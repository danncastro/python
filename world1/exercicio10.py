# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considera US$1,00 == R$3,27

valorCarteira = float(input('Quanto você tem na carteira? R$'))
dolar = valorCarteira / 5.36049
#dolar = valorCarteira / 3.27

print('Com R${:.2f} é possível comprar US${:.2f}'.format(valorCarteira, dolar))