"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para linguagem python
The Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.
"""

"""
[1] - Utilize Camel case para nomes de classes;
class Calculadora:
    pass


class CalculadoraCientifica:
    pass
"""
"""
[2] - Utilize nomes em minúsculo, separadores por underline para funções ou variáveis;
def soma():
    pass


def soma_dois():
    pass


numero = 4 

numero_impar = 5
"""
"""
[3] - Utilize 4 espaços para identação! (Não use Tab)
if 'a' in 'banana':
    print('tem')
"""
"""
[4] -  Linhas em branco
- Separar funções e definições de classe com deuas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;
class Classe:
    pass
"""

"""
[5] - Imports
- Imports devem ser sempre feitos em linhas separadas;

#Import Errado

import sys, os

#Import Certo
import sys
import os

#Não há problemas em utilizar:
from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:
from types import  (
    StringType,
    ListType,
    SetType,
    OutroType,
)
# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
# antes de constantes ou variáveis globais.
"""
"""
[6] - Espaços em expressões e instruções
#Não faça:
function( algo[ 1 ], { outro: 2 } )

#Faça:
function(algo[1], {outro: 2})

#Não faça:
algo (1)

#Faça
algo(1)

#Não faça:
dict['chave'] = list [indice]

#Faça
dict['chave'] = list[indice]

#Não faça
x               = 1
y               = 3
varieavel_longa = 5

#Faça
x  = 1
y  = 3
varieavel_longa = 5

"""
"""
[7] - Termine sempre uma instrução com uma nova linha

"""
