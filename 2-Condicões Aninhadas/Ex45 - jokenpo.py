#CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ.

#BIBLIOTECA PARA SELECIONAR NUMEROS ALEATÓRIOS
from random import randint
from time import sleep

print(f"{' JOKENPÔ ':=^40}")
#ITENS COMECANDO DO 0 ATÉ O 2
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print('''Escolha uma das opções: 
[  0  ] PEDRA
[  1  ] PAPEL
[  2  ] TESOURA \n ''')
jogador = int(input("Qual é a sua Jogada? "))

#FAZENDO ESPERAR 3 SEGUNDOS PARA APARECER A RESPOSTA
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1)
print("-=" * 11)
print(f"Computador jogou {itens[computador]}")
print(f"O jogador Jogou {itens[jogador]}")
print("-=" * 11)

#LÓGICA PARA COMPARAR AS ESCOLHAS
if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("OPÇÃO INVÁLIDA")
elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("OPÇÃO INVÁLIDA")