# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
# cada jogo, cadastrando tudo em uma lista composta.

#resolução
#pegar quantos jogos o jogador que fazer, sendo que cada jogo tem 6 números
#criar uma lista composta para jogar os números
#os numeros serao gerados de forma aleatória, de 1 a 60
#jogar os numeros sorteados para a lista composta

# Importa a função 'randint' para gerar números inteiros aleatórios
from random import randint
# Importa a função 'sleep' para adicionar uma pausa entre os sorteios
from time import sleep

# Cria uma lista vazia para armazenar números temporários durante o sorteio de cada jogo
lista = []
# Cria uma lista vazia para armazenar todos os jogos sorteados
jogos = []

# Exibe uma linha de separação com o título do programa
print("-=" * 30)
print("                   JOGA NA MEGA SENA      ")
print("-=" * 30)

# Solicita ao usuário que informe quantos jogos ele deseja que sejam sorteados
quant = int(input("Quantos jogos você quer que eu sorteie? "))

# Variável 'tot' é usada para contar o número de jogos sorteados
tot = 1

# Inicia um loop que vai continuar até o número de jogos sorteados atingir a quantidade solicitada pelo usuário
while tot <= quant:
    # Contador 'cont' usado para controlar quantos números foram sorteados para o jogo atual
    cont = 0
    # Enquanto 'cont' for menor que 6 (o número de números por jogo), sorteia números
    while True:
        # Gera um número aleatório entre 1 e 60 (inclusive)
        num = randint(1, 60)
        # Verifica se o número gerado ainda não foi adicionado à lista do jogo atual
        if num not in lista:
            lista.append(num)  # Se não, adiciona o número à lista
            cont += 1  # Incrementa o contador
        # Quando o contador atingir 6, sai do loop
        if cont >= 6:
            break
    # Organiza os números do jogo em ordem crescente
    lista.sort()
    # Adiciona uma cópia da lista atual de números sorteados à lista de jogos
    jogos.append(lista[:])
    # Limpa a lista para sorteio do próximo jogo
    lista.clear()
    # Incrementa o contador de jogos sorteados
    tot += 1

# Exibe uma linha de separação antes de exibir os jogos sorteados
print("-=" * 3,  f"  SORTEANDO {quant} JOGOS ", "-=" *3)

# Exibe os jogos sorteados um por um
for i, l in enumerate(jogos):
    # Exibe o número do jogo e a lista de números sorteados
    print(f"jogo {i + 1}: {l}")
    # Pausa de 1 segundo antes de exibir o próximo jogo (efeito visual)
    sleep(1)

# Exibe uma mensagem de boa sorte após exibir todos os jogos
print("-=" * 5, "< BOA SORTE! >", "-=" * 5)

