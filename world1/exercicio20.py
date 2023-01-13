# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia 
# o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

primeiroAluno = input('Primeiro aluno: ')
segundoAluno = input('Segundo aluno: ')
terceiroAluno = input('Terceiro aluno: ')
quartoAluno = input('Quarto aluno: ')

alunosSorteio = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]

shuffle(alunosSorteio)

print('A ordem de apresentação é \n', alunosSorteio)