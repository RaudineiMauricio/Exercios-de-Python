#Adapte o código do Exercicio 107, criando uma função adicional chamada moeda()
#que consiga mostrar os números como um valor monetário formatado.
import moedas

preco = float(input("Digite o preco: R$"))
print(f"A metade de {moedas.moeda(preco)} é {moedas.moeda(moedas.metade(preco))}")
print(f"O dobro de {moedas.moeda(preco)} é {moedas.moeda(moedas.dobro(preco))}")
print(f"Aumentando 10%, temos {moedas.moeda(moedas.aumentar(preco, 10))}")
