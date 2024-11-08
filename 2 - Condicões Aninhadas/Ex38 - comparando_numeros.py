#ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS MOSTRANDO NA TELA UMA MENSAGEM
# - O PRIMEIRO VALOR É MAIOR
# - O SEGUNDO VALOR É MAIOR
# - NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS

num1 = int(input("Digite o Primeiro Valor: "))
num2 = int(input("Dgitie  o Segundo Valor: "))

if num1 > num2:
    print("O PRIMEIRO VALOR É MAIOR!!")
elif num2 > num1:
    print("O SEGUNDO VALOR É MAIOR")
else:
    print("NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS")