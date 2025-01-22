#ESCREVA UM PROGRAMA PARA APROVAR UM EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA
#O PROGRAMA VAI PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
#CALCULE O VALOR DA PRESTAÇÃO MENSAL SABENDO QUE ELA NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGAGO.

valor_da_casa = float(input("Qual o valor da Casa? R$"))
salario = float(input("Quanto é o seu Sálario? R$"))  
anos = int(input("Em quantos anos deseja pagar? "))

#PARA SABER QUANTAS PRESTAÇOES IRÁ PAGAR, ANOS * 12 PARA SABER QUANTOS MESES 
prestacao = valor_da_casa / (anos * 12)
mínimo = salario * 1.3

print(f"Para pagar uma casa de R${valor_da_casa:.2f} em {anos} anos")
print(f"A prestação será de R${prestacao:.2f}")
#BLOCO DE CONDIÇÃO, SE O A PRESTAÇÃO FOR MENOR OU IGUAL AO SÁLARIO E LIBERADO SE NAO FOR SERÁ NEGADO
if prestacao <= mínimo:
    print("Emprestimo Autorizado!!")
else:
    print("Emprestimo Negado!!")