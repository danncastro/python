# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até '200Km' e R$0.45 para viagens mais longas

distanciaViagem = int(input('Qual a distância da viagem? ' ))

if distanciaViagem <= 200:
    print('Você percorreu {}Km e o custo da viagem é de R${:.2f}'.format(distanciaViagem, distanciaViagem * 0.50))
else:
    print('Você percorreu {}Km e o custo da viagem é de R${:.2f}'.format(distanciaViagem, distanciaViagem * 0.45))