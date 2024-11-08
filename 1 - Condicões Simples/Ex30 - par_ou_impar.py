#CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO  E MOSTRE NA TELA SE ELE É PAR ou ÍMPAR.

numero = int(input("Digite um número: "))
if numero % 2 == 0: #SE A SOBRA DA DIVISÃO POR 2 FOR 0 O NÚMERO É PAR SE NAO ELE É IMPAR
    print(f"O número {numero} É PAR")
else:
    print(f"O número {numero} é ÍMPAR")

