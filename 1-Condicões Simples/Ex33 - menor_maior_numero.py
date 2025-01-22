#FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR.

a = int(input("Digite o Primeiro número: "))
b = int(input("Digite o Segundo número: "))
c = int(input("Digite o Terceiro número: "))
#VERIFICANDO O MENOR VALOR
menor = a
if b < a and b < c :
    menor = b
if c < a and c < b:
    menor = c

#VERIFICANDO O MAIOR VALOR
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f"O MENOR VALOR DIGITADO FOI O {menor}")
print(f"O MAIOR VALOR DIGITADO FOI O {maior}")

