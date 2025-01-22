#  Faça um programa que tenha uma função chamada maior(),
#  que receba vários parâmetros com valores inteiros.
#  Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(* num):
    cont = maior = 0
    print("-=" * 30)
    print("Analisando valores passados...")
    for valor in num:
        print(f"{valor} ", end="", flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

    print(f" Foram analisados {cont} valores")
    print(f"O maior valor analisado foi {maior}")

    
#PROGRAMA PRINCIPAL
maior(2, 9, 4, 5, 2, 1)
maior(4, 7, 0)
maior(2, 1)
maior()