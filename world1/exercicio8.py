# Escreva m programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
# km hm dam m dm cm mm

medida = float(input('Digite a distãncia em metros: '))

cm = medida * 100
mm = medida * 1000
km = medida * 0.001
hm = medida * 0.01
dm = medida * 10
dam = medida * 0.1

print()
print('A medida de {}m corresponde a: '.format(medida))
print()
print('Centimetro: {:.0f}cm'.format(cm))
print('Milimetro: {:.0f}mm'.format(mm))
print('Quilometros: {:.3f}km'.format(km))
print('Hectómetros: {:.2f}hm'.format(hm))
print('Decímetros: {:.0f}dm'.format(dm))
print('Decâmetros: {:.1f}dam'.format(dam))
print()

