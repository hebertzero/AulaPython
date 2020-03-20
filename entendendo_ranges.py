"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utlizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

# Forma 1
Formas gerais:

range(valor_de_parada)
OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)


# Forma 2

range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)

# Exemplo forma 2
for num in range(1, 11):
    print(num)

# Forma 3

range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuario)

# Exemplo forma 3
for num in range(1, 10, 2):
    print(num)

# Forma 4 (Inversa)

range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (valor_inicio especificado pelo usuário, e passo especificado pelo usuario)

# Exemplo forma 4
for num in range(10, 0, -1):
    print(num)
"""

