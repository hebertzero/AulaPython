"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais;
    - Variáveis globais são reconhecidas, ou  seja, seu escopo compreende, todo o programa.
2 - Variáveis locais;
    - Varáveis locais são reconhecidas apens no bloco onde foram declarads, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_de_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinânima. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuimos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""

numero = 42
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

numero = 42
# novo = 0

if numero > 10:
    novo = numero + 10 # A variável 'novo' está declarada localmente dentro do bloco do if.Portanto, é local
    print(novo)