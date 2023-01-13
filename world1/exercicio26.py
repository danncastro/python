# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez;

frase = input('Digite um frase: ').strip()
print()

print('A letra "A" é encontra [{}] vezes'.format(frase.upper().count("A")))

print('e aparece pela primeira vez na posição [{}]'.format(frase.find("A")+1))

fraseUltima = frase
print('sua última posição foi [{}]'.format(frase.rfind("A")+1))