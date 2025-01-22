#Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
#informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
#desenvolvida no desafio 108.
import moedas

preco = float(input("Digite o preco: R$"))
print(f"A metade de {moedas.moeda(preco)} é {(moedas.metade(preco, True))}") #se quiser sem formatacao coloque false.
print(f"O dobro de {moedas.moeda(preco)} é {(moedas.dobro(preco, True))}")
print(f"Aumentando 10%, temos {(moedas.aumentar(preco, 10, True))}")
print(f"Reduzindo 13%, temos {moedas.diminuir(preco, 13, True)}")