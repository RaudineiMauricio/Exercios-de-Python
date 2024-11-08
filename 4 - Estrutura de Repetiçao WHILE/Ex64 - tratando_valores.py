#CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO.
#O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR 999, QUE É A CONDIÇÃO DE PARADA.
#NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES, (DESCONSIDERANDO O FLAG)


cont = numero = soma = 0
numero = int(input("Digite um Valor [999 para Parar]: "))
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input("Digite um Valor [999 para Parar]: "))
print(f"Foram registrados {cont} numeros e a soma entre eles foi {soma} ")

'''cont = 0
numero = 0
soma = 0
while numero != 999:
    numero = int(input("Digite um Valor: "))
    
    if numero == 999:
        print("Fim do Programa")
    else:
       cont +=1
       soma = numero + soma
print(f"Foram registrados {cont} numeros e a soma entre eles foi {soma} ")'''