#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista
#e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint  # Importa a função randint da biblioteca random para gerar números aleatórios.
from time import sleep      # Importa a função sleep da biblioteca time para adicionar uma pausa no programa.

# Função que sorteia 5 números aleatórios e os adiciona à lista recebida como parâmetro.
def sorteia(lista):

    print("Sorteando 5 valores da lista: ", end="")  # Imprime uma mensagem inicial sem quebrar a linha.
    for cont in range(5):  # Loop que itera 5 vezes para sortear 5 números.
        n = randint(1, 10)  # Gera um número aleatório entre 1 e 10.
        lista.append(n)  # Adiciona o número sorteado à lista.
        print(f"{n} ", end="", flush=True)  # Imprime o número sorteado, mantendo o texto na mesma linha.
        sleep(0.4)  # Adiciona uma pausa de 0,4 segundos entre a impressão dos números.
    print("PRONTO") 

# Imprime "PRONTO" ao final do sorteio.

# Função que soma os números pares de uma lista recebida como parâmetro.
def somar_par(lista):  
    soma = 0  # Inicializa a variável que armazenará a soma dos números pares.
    for valor in lista:  # Percorre todos os valores da lista.
        if valor % 2 == 0:  # Verifica se o valor atual é par.
            soma += valor  # Soma o valor à variável 'soma' se for par.
    print(f"Somando os valores pares de {lista}, temos {soma}")  # Exibe o resultado da soma dos números pares.

# Programa principal
numeros = list()  # Cria uma lista vazia para armazenar os números sorteados.
sorteia(numeros)  # Chama a função sorteia para preencher a lista com 5 números aleatórios.
somar_par(numeros)  # Chama a função somar_par para somar os números pares da lista.

