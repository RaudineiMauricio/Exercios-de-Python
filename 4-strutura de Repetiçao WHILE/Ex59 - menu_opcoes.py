#CRIE UM PROGRAMA QUE LEIA DOIS  VALORES E MOSTRE UM MENU NA TELA:
#[1] SOMAR
#[2] MULTIPLICAR
#[3] MAIOR
#[4] NOVOS NÚMEROS
#[5] SAIR DO PROGRAMA
#SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO
from time import sleep
num1 = int(input(f"Digite o Primeiro valor: "))
num2 = int(input(f"Digite o Segundo valor: "))
opcao = 0
while opcao != 5:
    print(''' MENU DE OPÇÕES
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        soma = num1 + num2
        print(f"A Soma de {num1} + {num2}  é {soma}")
    elif opcao == 2:
        multiplicacao = num1 * num2
        print(f"A Multiplicação de {num1} x {num2} é {multiplicacao}")
    elif opcao == 3:
        if num1 > num2:
           maior = num1
        else:
            maior = num2
        print(f"O maior numero entre {num1} e {num2} é {maior}")
    elif opcao == 4:
        print("Escolha outros valores!")
        num1 = int(input(f"Digite o Primeiro valor: "))
        num2 = int(input(f"Digite o Segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção Inválida")
    print('=-=' * 10)
    sleep(1)
print("Fim do Pragrama Volte Sempre!")
        