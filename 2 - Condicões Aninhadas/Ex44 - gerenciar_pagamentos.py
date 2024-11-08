#ELABORE UM PROGRAMA QUE CALCULE UM VALOR A SER PAGO POR UM PRODUTO,
#CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:
# - À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
# - À VISTA NO CARTÃO: 5% DE DESCONTO
# - EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
# - 3X OU MAIS NO CARTÃO: 20% DE JUROS

print(f"{' LOJA JOGA10 ':=^40}")
produto = float(input("Qual o valor do Produto?R$"))

#LISTA PARA OPÇOES, AS ''' AJUDA A USAR VARIAS LINHAS.
print('''Escolha a forma de pagamento:
        [ 1 ] À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
        [ 2 ] À VISTA NO CARTÃO: 5% DE DESCONTO
        [ 3 ] EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
        [ 4 ] 3X OU MAIS NO CARTÃO: 20% DE JUROS\n''')

opcao = int(input("Sua Opção: "))
#LÓGICA PARA CALCULOS
if opcao == 1:
    valor = produto * 0.9
    print(f"Para pagamento em Dinheiro/Cheque o valor é de R${valor:.2f}, voce teve 10% de desconto! ")
elif opcao == 2:
    valor = produto * 0.95
    print(f"Para pagamento no Cartão o Valor é de R${valor:.2f}, Voce teve 5% de desconto! ")
elif opcao == 3:
    valor = produto
    total_pacerlas = produto / 2
    print(f"Sua compra Será parcela em 2x de R${total_pacerlas} Sem juros!!")
    print(f"Para pagamento em até 2x, o Valor é de R${valor:.2f} e voce não teve desconto!!")
elif opcao == 4:
    valor = produto * 1.2
    total_pacerlas = int(input("Quantas Parcelas? "))
    parcela = valor / total_pacerlas
    print(f"Sua compra será parcelada em {total_pacerlas}x de R${parcela:.2f} com juros de 20%")
    print(f"Sua compra de R${produto:.2f} vai custar R${valor:.2f} no Final ")
else:
    print("Opção Inválido para pagamento, Tente Novamente!!")