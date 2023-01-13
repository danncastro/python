# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar '80Km/h' mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7,00 por cada Km acima do limite.

velCar = float(input('Digite a velocidade do carro: '))

if velCar <= 80:
    print('Velocidade permitida, boa viagem')
else:
    print('Velocidade acima do permitido [80], multa no valor de R${:.2f}'.format((velCar-80) * 7))