# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número: '))
print()

# Utilizando o método comum
print('O dobro de {} é {} \n o seu triplo é {} \n e sua raiz quadrada é {:.2f}'.format(numero, (numero*2), (numero*3), (numero**(1/2))))