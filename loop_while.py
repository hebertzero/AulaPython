"""
Loop while

Forma geral

While expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão Booleada é expressão onde resultado é verdadeiro ou falso.

Exemplo:
num = 5

num < 5

# Exemplo 1

numero = 1

while numero < 10:
    print(numero)
    numero = numero * 2

# OBS: Em um loop while, é importante que cuidamos do critério de parada para não causar um loop infinito.
"""


# Exemplo 2

resposta = ' '

while resposta != 'sim':
    resposta = input('Ja acabou Jessica? ')