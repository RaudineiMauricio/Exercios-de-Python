#FAÇA UM PROGRAMA ONDE O COMPUTADOR VAI "PENSAR" EM UM NÚMERO ENTRE 0 E 10.
#O JOGADOR VAI ADIVINHAR ATÉ ACERTAR,
#  MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENCER.
from random import randint  # Importa a função randint do módulo random para gerar números aleatórios

computador = randint(0, 10)  # O computador escolhe um número aleatório entre 0 e 10
print("Sou seu Computador...Acabei de pensar em um número entre 0 e 10")  # Mensagem informando que o computador escolheu um número
print("Será que voce consegue advinhar qual foi?")  # Pergunta ao jogador se ele consegue adivinhar o número

acertou = False  # Inicializa a variável 'acertou' como False, indicando que o jogador ainda não acertou
palpites = 0  # Inicializa o contador de palpites como 0

while not acertou:  # Enquanto o jogador não acertar o número
    jogador = int(input("Qual é o seu palpite: "))  # Solicita ao jogador que insira um palpite e converte para inteiro
    palpites += 1  # Incrementa o contador de palpites

    if jogador == computador:  # Verifica se o palpite do jogador é igual ao número escolhido pelo computador
        acertou = True  # Se o palpite estiver correto, muda 'acertou' para True
    else:  # Se o palpite estiver incorreto
        if jogador < computador:  # Verifica se o palpite é menor que o número do computador
            print("Mais... Tente Mais uma vez!")  # Informa ao jogador que o número é maior
        elif jogador > computador:  # Verifica se o palpite é maior que o número do computador
            print("Menos... Tente mais uma vez!")  # Informa ao jogador que o número é menor

print(f"Acertou com {palpites} Palpites")  # Exibe a quantidade de palpites que o jogador fez até acertar