#FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS. NO FINAL, MOSTRE QUAL FOI O MAIOR E MENOR PESO LIDOS.

#Entendimento

#ler os pesos das 5 pessoas
#comparar o peso que foi digitado um com o outro das 5 pessoas
#mostra o maior e o menor peso
menor_peso = 0
maior_peso = 0
for p in range(1,6):
    peso = float(input(f"Qual o peso da {p}° Pessoa? "))
    if p == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f"O maior peso lido foi {maior_peso}kg e o menor peso {menor_peso}kg")

    
    





