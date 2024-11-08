#CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL, MOSTRE QUANTAS
#PESSOAS AINDA NAO ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES.

#PEGAR 7X O ANO DE NASCIMENTO -> DESCOBRIR QUANTAS PESSOAS AINDA TEM MENOS DE 18 ANOS, E QUANTAS TEM MAIS DE 18.

from datetime import date
maior_idade = 0 #QUARDA AS IDADES QUE SAO MAIORES QUE 18
menor_idade = 0 #GUARADA AS MENORES IDADES
for c in range(1, 8):
    nascimento = int(input(f"Ano de Nascimento da {c}° Pessoa: "))
    idade = date.today().year - nascimento
    if idade >= 18:
        maior_idade +=1 #SE ATENDER, JOGA LÁ PRA VARIAVEL QUE ARMAZENA AS MAIORES IDADES
    elif idade < 18:
        menor_idade +=1
print(f"Ao todo tivemos {maior_idade} pessoas Maiores de idade e {menor_idade} Menores de idade ")


    

    
