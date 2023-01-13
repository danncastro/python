# Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento.

salarioFuncionario = float(input('Salário funcionario R$'))

aumento = salarioFuncionario + (salarioFuncionario * 15 / 100)

print('Salário anterio R${:.2f}, com aumento de 15%, o valor passa a ser R${:.2f}'.format(salarioFuncionario, aumento))