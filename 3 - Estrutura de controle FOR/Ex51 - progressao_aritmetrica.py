#DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA  Progressão Aritmética (P.A.) 
#NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PRORESSÃO

# Solicita ao usuário o primeiro termo da PA
primeiro = int(input("Primeiro Termo: "))

# Solicita ao usuário a razão da PA
razao = int(input("Razao: "))

# Calcula o décimo termo da PA usando a fórmula do n-ésimo termo
decimo = primeiro + (10 - 1) * razao

# Imprime a mensagem inicial para os termos da PA
print("Termos da PA:")

# Loop para gerar os termos da PA
# A função range inicia em 'primeiro' e vai até 'decimo + razao' com passo 'razao'
for c in range(primeiro, decimo + razao, razao):
    # Imprime cada termo seguido de " -> "
    print(c, end=" -> ")

# Após o loop, imprime "ACABOU" para indicar que a sequência terminou
print("ACABOU")
