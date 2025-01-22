#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
#Faça também um programa que importe esse módulo e use algumas dessas funções.

import moedas

preco = float(input("Digite o preco: R$"))
print(f"A metade de R${preco} é {moedas.metade(preco)}")
print(f"O dobro de R${preco} é {moedas.dobro(preco)}")
print(f"Aumentando 10%, temos R${moedas.aumentar(preco, 10)}")
