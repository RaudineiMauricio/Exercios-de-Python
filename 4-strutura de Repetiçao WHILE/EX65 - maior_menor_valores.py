#CRIE UM PROGRMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO.
#NO FINAL DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE TODOS OS VALORES
#E QUAL FOI O MAIOR E O MENOR VALORES LIDOS. O PROGRAMA DEVE PERGUNTAR AO USUÁRIO
#SE ELE QUER OU NAO CONTINUAR A DIGITAR VALORES.

# Inicializa as variáveis soma, quant, media, maior e menor com 0
soma = quant = media = maior = menor = 0

# Define a variável resp como "S" para iniciar o loop
resp = "S"

# Inicia um loop que continuará enquanto a resposta for "S" ou "s"
while resp in "Ss":
    # Solicita ao usuário que digite um número e converte a entrada para um inteiro
    num = int(input("Digite um número: "))
    
    # Adiciona o número digitado à soma total
    soma += num
    
    # Incrementa a contagem de números digitados
    quant += 1
    
    # Se for o primeiro número digitado, inicializa maior e menor com esse número
    if quant == 1:
        maior = menor = num
    else:
        # Se o número digitado for maior que o atual maior, atualiza maior
        if num > maior:
            maior = num
        # Se o número digitado for menor que o atual menor, atualiza menor
        if num < menor:
            menor = num
    
    # Pergunta ao usuário se deseja continuar a entrada de números
    resp = str(input("Quer Continuar? [S/N] "))

# Calcula a média dos números digitados
media = soma / quant

# Exibe a quantidade de números digitados e a média
print(f"Voce digitou {quant} números e a média foi {media} ")

# Exibe o maior e o menor valor digitado
print(f"O maior valor foi {maior} e o menor foi {menor}")