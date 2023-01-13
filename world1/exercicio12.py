# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valorProduto = float(input('Qual é o preço do produto R$'))
desconto = valorProduto - (valorProduto * 5 / 100)

print('O produto custa R${:.2f}, na promoção com 5% de desconto custará R${:.2f}'.format(valorProduto, desconto))