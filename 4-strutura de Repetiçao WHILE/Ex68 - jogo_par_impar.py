#FAÇA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O COMPUTADOR.
#O JOGO SÓ SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER, MOSTRANDO O TOTALDE 
#VITORIAS CONSECUTIVAS QUE ELE CONQUISTOU NO FINAL DO JOGO.
from random import randint

v = 0  # Variável para contar as vitórias do jogador

while True:
    # Solicita um valor ao jogador
    jogador = int(input("Digite um valor: "))
    
    # O computador escolhe um número aleatório entre 0 e 10
    computador = randint(0, 10)
    
    # Calcula o total dos números
    total = jogador + computador
    tipo = " "
    
    # Pergunta se o jogador quer escolher "P" ou "I" (Par ou Ímpar)
    while tipo not in "PI":
        tipo = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    
    # Exibe os valores jogados e o total
    print(f"Você jogou {jogador} e o computador jogou {computador}. Total de {total} ", end=" ")
    print("DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")
    
    # Verifica se o jogador venceu ou perdeu
    if tipo == "P":
        if total % 2 == 0:
            print("Você Venceu!")
            v += 1
        else:
            print("Você PERDEU!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você Venceu!")
            v += 1
        else:
            print("Você PERDEU!")
            break
    
    # Informa que o jogo continuará
    print("Vamos jogar novamente...")
    
# Ao final, exibe o número de vitórias
print(f"GAME OVER! Você venceu {v} vez(es).")


