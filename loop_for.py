"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

C ou java:

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python
for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplo de iteráveis:
- String
    nome = 'Geek university'
- Lista
    lista = [1, 2, 3, 4, 5]
- Range
    numeros = range(1, 10)
"""
"""
nome = 'geek university'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transfomar em uma lista

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numeros in lista:
    print(numeros)

# Exemplo de for 3 (Iterando sobre um range)

# range(valor_inicial, valor_final)
# OBS: O valor final não é inclusive.
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10 - Não

for numeros in range(1, 10):
    print(numeros)
"""

nome = 'geek university'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

"""
Enumerate:
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4,' '), (5, 'U'), (6, 'n'), (7, 'i'), (8, 'v'), (9, 'e'),
(10, 'r'), (11, 's'), (12, 'i'), (13, 't'), (14, 'y'))

for i, v in enumerate(nome):
    print(nome[indice])
"""
"""
nome = 'geek university'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for indice, letra in enumerate(nome):
    print(letra)
    
for valor in enumerate(nome):
    print(valor)


"""
"""
for _, letra in enumerate(nome):
    print(letra)
    
OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)
"""

# qtd = int(input('Quantas vezes esse loop deve rodar? '))

# for n in range(1, qtd):
# print(f'Imprimindo {n}')
"""
qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'geek university'
for letra in nome:
    print(letra, end=' ') 
"""

# Original: U+1F60D
# Modificado: U0001F60D


for x in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)