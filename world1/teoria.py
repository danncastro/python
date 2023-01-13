# Operadores aritméticos:
# 5 + 5 == 7 (Soma)
# 5 - 2 == 3 (Subtração)
# 5 * 2 == 10 (Multiplicação)
# 5 / 2 == 2.5 (Divisão real)
# 5 ** 2 == 25 (Exponenciação)
# 5 // 2 == 2 (Divisão inteira)
# 5 %¨2 == 1 (Resto da divisão)

# Ordem de precedêcia
# 1 == ()
# 2 == ** 
# 3 == * / // %
# 4 == + -

# Exemplos de ordem de precedencias
precedencia4 = 5+3*2
print(precedencia4)

precedencia2 = 3*5+4**2
print(precedencia2)

precedencia1 = precedencia2 = 3*(5+4)**2
print(precedencia1)

# Função interna de potência
# Não tem ordem de precedência
# pow(valor1, valor2) 

# Exemplos interessantes:
# print('Mensagem {:=^20}!'.format(variavel))

# Exemplos de formatação de casas decimais
# print('A soma é {:.3f}'.format(variave))

# Exemplos de formatação sem quebra de linha
# print('A soma é {:.3f}'.format(variavel), end=' ')

# Exemplos de formatação com quebra de linha
# print('A soma é {}, \n o produto é {}, a divisão é {:.3f}'.format(variavel, variavel, variavel))

# Módulos
# import modulo (Importa todas funcionalidades(bibliotecas) contidas no módulo)
# from biblioteca importe modulo (Importa apenas a funcionalidades(bibliotecas) expecificas)
# exemplo:
# import math
# from math import sqrt

# Cadeia de caracteres
# Exemplo
# fatiamento = '[C][u][r][s][o]   [e][m]   [V][ i][ d][ e][ o]    [ P][ y][ t][ h][ o][ n]'
#               [0][1][2][3][4][5][6][7][8][9][10][11][12][13][14][15][16][17][18][19][20] 

# print('frase[9:13]') - Começa no 9° caracter até o 12º
# print('frase[9:21]') - Começa no 9° caracter até o 20º
# print('frase[9:21:2]) - Começa no 9º até o 20° pulando de 2 em 2
# print('frase[15:]') - Começa no 15º até o final da frase
# print('frase[:5]') - Começa no inicio da frase até o 4° caracter
# print('frase[9::3]') - Começa no 9º caracter, até o final da frase, pulando de 3 em 3

# Analise
# Exemplo
# len(frase) - Mostra o comprimento da frase
# frase.count('o') - Conta quantas letras dentro da aspas tem na frase
# frase.count('o', 0, 13) - Conta quantas letras dentro da aspas tem na frase, do 0º até o 12º
# frase.find('deo') - Informa em qual posição encontra os caracteres dentro das aspas
# frase.rfind('deo') - Informa em qual posição encontra os caracteres contando da direita para esquerda
# print('palavra' in frase) - Valida se existe a palavra dentro da frase

# Transformação
# Exemplo
# frase.replace('Python', 'Android') - Substitui uma frase pela outra
# frase.upper() - Transforma todas as letras minusculas em maiusculas
# frase.lower() - Transforma todas as letras maiusculas em minusculas
# frase.capitalize() - Transforma todas as letras maiusculas em minusculas exeto a primeira letra
# frase.title() - Transforma todas letras iniciais em maiusculas
# frase.strip() - Remove os espaços não utilizados no começo e no final da frase
# frase.rstrip() - Remove os espaços vazios do lado direto da string
# frase.lstrip() - Remove os espaços vazios do lado esquerdo da string

# Divisão
# Exemplo
# frase.split() - Cria uma divisão aonde há espaços da string, gerando uma lista separada por frases

# Junção
# Exemplo
# '-'.join(frase) - Adiciona o que está entre aspas dentro dos espaços vazios da frase

# Condições (Estrutura condicional)
# Ex:
# se carro.viraresquerda()
# if carro.esquerda(): - Sempre coloque os 2 pontos no final da função
#   bloco _V_
#   bloco True
# senão carro.virardireita()
# else carro.direita():
#   bloco _F_
#   bloco False

# Exemplo condição simplificada
# tempo = int(input('Quantos anos tem seu carro?'))
#print('carro novo' if tempo<=3 else 'carro velho')
#print('--FIM--')