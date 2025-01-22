#CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS
#A CADA PESSOA CADASTRADA, O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO QUER OU NÃO CONTINUAR
#NO FINAL, MOSTRE:
#A) QUANTAS PESSOAS TEM MAIS DE 18 ANOS
#B) QUANTOS HOMENS FORAM CADASTRADOS
#C) QUANTAS MULHERES TEM MENOS DE 20 ANOS

homem = mulher = menor_idade = maior_idade = pessoa = 0

while True:
    print("-" * 20)
    print(f"CADASTRO DE PESSOAS")
    print("-" * 20)
    idade = int(input("Digite Sua idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Digite seu Sexo: [M/F] ")).strip().upper()[0]

    if sexo == "F":
        mulher += 1
    else:
        homem += 1
    if idade >=18:
        pessoa +=1
        maior_idade += 1
    if sexo == "F" and idade < 20:
        menor_idade += 1
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if resposta == "N":
        print("Cadastros Finalizados!!")
        break
print(f"Total de pessoas com mais de 18 anos {pessoa} pessoas")
print(f"foram cadastrados {homem} homens, e {menor_idade} mulheres com menos de 20 anos")
