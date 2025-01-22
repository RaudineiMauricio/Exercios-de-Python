#CRIE UM PROGRAMA QUE LEIA NÚMEROS INTEIROS PELO TECLADO.
#O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR A 999, QUE É A CONDIÇÃO DE PARADA.
#NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELE(DESCONSIDENRANDO O FLAG)

quantidade = 0
soma = 0
while True: #O true gera um loop infinito e o break  faz a parada do loop quando for
    #digitado o 999.
    numero = int(input("Digite um valor [999 para parar]: "))
    if numero == 999:
        break   
    quantidade += 1
    soma += numero
print(f"Foram registrados {quantidade} numeros e a soma dos valores foi {soma}")
