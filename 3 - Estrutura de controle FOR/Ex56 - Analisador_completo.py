#DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS.
#NO FNAL DO PROGRAMA, MOSTRE: A MÉDIA DE IDADE DO GRUPO 
#QUAL É O NOME DO HOMEM MAIS VELHO
#E QUANTAS MULHERES TEM MENOS DE 20 ANOS.

'''pegar os nomes, idade e sexo na mesma opçao - OK

somar todas as idades e dividir por 4 OK

armazenar em uma variavel o nome do homem mais velho

e armazenar as idades das mulheres pra ver quem tem menos de 20 anos se tiver'''
# Inicializa variáveis para armazenar o nome do homem mais velho, 
# a maior idade encontrada, a soma das idades, e a contagem de mulheres com menos de 20 anos.
mais_velho = ""  # Nome do homem mais velho
maior_idade = 0  # Maior idade entre os homens
soma_idade = 0   # Soma das idades de todas as pessoas
mulheres_menores_20 = 0  # Contador de mulheres com menos de 20 anos

# Laço para repetir 4 vezes, uma para cada pessoa.
for d in range(1, 5):
    # Recebe o nome da pessoa
    nome = input("Digite seu nome: ")
    
    # Recebe a idade da pessoa e converte para inteiro
    idade = int(input("Quantos anos você tem? "))
    
    # Recebe o sexo da pessoa, removendo espaços e convertendo para maiúsculo
    sexo = input("Qual o seu sexo? M/F: ").strip().upper()

    # Adiciona a idade ao total da soma das idades
    soma_idade += idade

    # Verifica se a pessoa é do sexo masculino e se tem a maior idade até o momento
    if sexo == "M" and idade > maior_idade:
        maior_idade = idade  # Atualiza a maior idade
        mais_velho = nome  # Armazena o nome do homem mais velho

    # Verifica se a pessoa é do sexo feminino e tem menos de 20 anos
    if sexo == "F" and idade < 20:
        mulheres_menores_20 += 1  # Incrementa o contador de mulheres com menos de 20 anos

# Calcula a média de idade do grupo
media_idade = soma_idade / 4

# Exibe a média de idade formatada com uma casa decimal
print(f"A média de idade é {media_idade:.1f} anos.")

# Verifica se há algum homem no grupo e exibe o nome e idade do mais velho
if mais_velho:
    print(f"O homem mais velho é {mais_velho} com {maior_idade} anos.")
else:
    print("Não há homens no grupo.")

# Exibe a quantidade de mulheres com menos de 20 anos
print(f"Há {mulheres_menores_20} mulher(es) com menos de 20 anos.")  