"""
Estrutura condicionais
if, else, elif
"""

idade = 18

"""
# Estrutura condicional if, else em C
if(idade < 18){
    printf("Menor de idade");
}else if(idade == 18){
    printf("Tem 18 anos");
}else{
    prinf("É maior de idade");
}
"""

"""
# Estrutura condicional if, else em Java
if(idade < 18){
    System.out.println("Menor de idade");
}else if(idade == 18){
    System.out.println("Tem 18 anos");
}else{
   System.out.println("É maior de idade");
}
"""

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')


if idade < 18:
    print('Menor de idade')

if idade == 18:
    print('Tem 18 anos')

if idade == 26:
    print('Tem 26 anos')

if idade > 18:
    print('Maior de idade')