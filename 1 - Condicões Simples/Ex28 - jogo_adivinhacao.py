#Escreva um programa que faça o COMPUTADOR "pensar" em um número inteiro entre 0 e 5 
#e peça para o USUÁRIO tentar descobrir qual foi o número escolhido pelo computador
#O programa deverá escrever na tela se o usuário ganhou ou perdeu.


#IMPOTANDO UM COMPONENTE DA BIBLIOTECA PARA SORTEAR UM NÚMERO
from random import randint
from time import sleep #sleep faz esperar quantos segundos voce desejar

computador = randint(0, 5) #FAZ O COMPUTADOR "PENSAR"
print("-=-"*20) #PARA CRIAR UMA DECORACAO
print("Vou pensar em um número entre 0 e 5, Tente Adivinhar...")
print("-=-"*20)
jogador = int(input("Em que número eu pensei? ")) #JOGADOR TENTA ADIVINHAR
print("PROCESSANDO...")
sleep(2)
#BLOCO DE CONDICOES
if computador == jogador:
    print("PARABÉNS!! Voce conseguir me vencer!!")
else:
    print(f"GANHEI!!, Eu pensei no {computador} e não no {jogador}")



