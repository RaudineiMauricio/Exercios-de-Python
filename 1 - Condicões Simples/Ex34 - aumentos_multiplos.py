#ESCREVA UM PROGRAMA QUE PERGUNTE O SÁLARIO DE UM FUNCIONÁRIO E CALCULE O VALOR DE SEU AUMENTO
#PARA SÁLARIOS SUPERIORES A R$1250,00, CALCULE UM AUMENTO DE 10%. PARA OS INFERIORES OU IGUAIS O AUMENTO É DE 15%

salario = float(input("Qual o valor do sálario do Funcionário:R$ "))
if salario > 1250:
    novo = (salario * 0.10)
    print(f"O valor do aumento foi de R${novo} ")
if salario <= 1250:
    novo = (salario * 0.15)
    print(f"O valor do Aumento foi de R${novo}")
print(f"O Novo sálario do Funcionário é de R${salario + novo}")