#A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA
#CATEGORIA. DE ACORDO COM A IDADE:
# - ATÉ 9 ANOS: MIRIM
# - ATÉ 14 ANOS:INFANTIL
# - ATÉ 19 ANOS: JÚNIOR
# - ATÉ 25 ANOS: SÊNOR
# - ACIMA DE 25 ANOS : MASTER
from datetime import date
atual = date.today().year
ano_nascimento = int(input("Qual ano de Nascimento? "))
idade = atual - ano_nascimento

#LÓGICA PARA PERCORRER E DESCOBRIR QUAL IDADE ATENDE O REQUISITO.
if idade <= 9:
    print(f"Voce tem {idade} anos e Sua categoria é MIRIM")
elif idade <= 14:
    print(f"Voce tem {idade} anos e sua Categoria é INFANTIL")
elif idade <= 19:
    print(f"Voce tem {idade} anos e sua Categoria é JÚNIOR")
elif idade <=25:
    print(f"Voce tem {idade} anos e sua Categoria é SÊNOR")
else:
    print(f"Voce tem {idade} anos e sua Categoria é MASTER")