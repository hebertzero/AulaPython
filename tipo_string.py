"""
Tipo string

Em python, um dado é considerado do tipo string sempre que:
- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = 'Angelina \" Jolie'
print(nome)
print(type(nome))


nome = 'Geek University'
print(nome.upper())

nome = 'Geek University'
print(nome.lower())

nome = 'Geek University'
print(nome.split()) #  transforma em uma lista de strings
"""
# Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

# [0,    1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13,  14]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
nome = 'Geek University'
print(nome[0:4])  # slice de string

print(nome[5:15])  # slice de string
# [     0,           1 ]
# ['Geek', 'University']
print(nome.split())
print(nome.split()[0])
print(nome.split()[1])

"""
[::-1] -> Come do primiro elemento, vá até o último elemento e inverta
"""
print(nome[::-1])  # Inversão da String pythônico

print(nome.replace('e', 'P'))
