#FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ,
#PARA CADA VALOR DIGITADO PELO USUÁRIO.
#O PROGRAMA SERÁ INTERROPMPIDO QUANDO O NÚMERO SOLICITADO FOR NEGATIVO.




while True:
    num = int(input("Digite um numero para ver a sua tabuada [-1 PARA PARAR]: "))
    if num < 0:
        break #AQUI O BREAK PARA O PROGRAMA SE DIGITAR QUALQUER NÚMERO NEGATIVO
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i} ") 
print("PROGRAMA TABUADA ENCERRADO. Volte Sempre!!")

#ESSE BLOCO DE CÓDIGO ABAIXO EU ACABEI CRIANDO PARA PERGUNTAR O USUÁRIO SE ELE QUER CONTINUAR, E COM A RESPOSTA "N" ENCERRAR O PROGRAMA
'''resposta = str(input("Deseja Continuar? [S/N] ")).upper().split()[0]
    if resposta == "S":
        num = int(input("Digite um numero para ver a sua tabuada [-1 PARA PARAR]: "))
    elif resposta == "N":
        break'''

