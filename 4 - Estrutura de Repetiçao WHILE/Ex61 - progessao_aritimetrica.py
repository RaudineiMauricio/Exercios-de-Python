#REFAÇA O EXERCICIO 51, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA,
#MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSAO USANDO A ESTRUTURA WHILE.

print("GERADOR DE PA")
print("-=-" * 10)
primeiro = int(input("Digite o Primeiro: "))
razao = int(input("Digite a Razão  da PA: "))
termo = primeiro
cont = 1
while cont <= 10:
    print(f"{termo} -> ", end="")
    termo += razao
    cont+=1
print("FIM")
