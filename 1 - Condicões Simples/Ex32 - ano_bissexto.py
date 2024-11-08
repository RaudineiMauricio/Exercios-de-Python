#CRIE UM PROGRAMA QUE MOSTRE SE O ANO É BISSEXTO
# Se o ano não termina em 00, ele é bissexto caso seja divisível por 4. 
# Exemplos: 1988, 1992, 1996, 2004, e assim por diante. Nota:
# Um número é divisível por 4 se a sua dezena (1988 = 88) é divisível por 4.
from datetime import date
ano = int(input("Que ano quer Analisar? Coloque 0 para análisar o ano Atual: "))

#CONDICAO PARA O ANO SER CALCULADO
#A DIVISAO DO ANO POR 4 TEM QUE SER 0, O ANO NAO PODE SER
# DIVISIVEL POR 100,  OU ANO DIVIDIO POR 400 SER IGUAL A 0
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é BISSEXTO!!")
else:
    print(f"O ano {ano} não é BISSEXTO")
