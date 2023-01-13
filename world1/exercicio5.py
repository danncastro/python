# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

numeroInteiro = int(input('Digite um número inteiro: '))
print()

antecessor = numeroInteiro - 1
sucessor = numeroInteiro + 1

print('Utilizando variaveis')
print('O antecessor do número {} é {}, e seu sucessor é {}'.format(numeroInteiro, antecessor, sucessor))
print()

print('Sem utilizar variaveis')
print('O antecessor do númer {} é {}, e seu sucessor é {}'.format(numeroInteiro, (numeroInteiro-1), (numeroInteiro+1)))