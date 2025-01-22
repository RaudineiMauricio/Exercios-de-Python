#CRIE UM PROGRAMA QUE LEIA O NOME E OS PREÇOS DE VARIOS PRODUTOS.
#O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR OU NÃO. NO FINAL MOSTRE:
#A) QUAL O VALOR GASTO DA COMPRA
#B) QUANTOS PRODUTOS CUSTAM MAIS DE R$1000,00
#C) QUAL É O NOME DO PRODUTO MAIS BARATO

maior1k = total = menor_valor = cont =  0
resp = " "
barato = ""
while True:
    produto = str(input("Digite o nome do Produto: "))
    valor = float(input("Valor do produto: R$"))
    total += valor
    cont += 1 
    resp = str(input("Deseja Continuar? [S/N] ")).strip().upper()[0]
    
    if valor > 1000:
        maior1k += 1
    if cont == 1 or valor < menor_valor:
        menor_valor = valor
        barato = produto
   
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N] "))
    if resp == "N":
        break
print("Fim do Programa!!")
print(f"O valor da sua compra foi R${total:.2f}" )
print(f"{maior1k} produtos custam mais de R$1000, o produto mais barato custa R${menor_valor:.2f} que foi o {barato}")