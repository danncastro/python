# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

larguraParede = float(input('Largura parede: '))
alturaParede = float(input('Altura parede: '))
area = larguraParede * alturaParede

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larguraParede, alturaParede, area))
print('Para pintar essa parede, será necessário, {}L de tinta.'.format(area/2))