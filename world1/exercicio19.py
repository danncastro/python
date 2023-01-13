# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles
# escrevendo o nome sorteado.

import random

primeiroAluno = input('Primeiro aluno: ')
segundoAluno = input('Segundo aluno: ')
terceiroAluno = input('Terceiro aluno: ')
quartoAluno = input('Quarto aluno: ')

alunosSorteio = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]

sorteado = random.choice(alunosSorteio)

print('O aluno escolido foi {}'.format(sorteado))