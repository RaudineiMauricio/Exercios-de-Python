#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:                                                                                                                                            
# A) Quantos números foram digitados.                                                                                                                    
# B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.

tot = 0
num = []
while True:
    num.append(int(input("Digite um valor: ")))
    tot += 1
    
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print("-=" * 30)
print(f"sua Lista {num}")
print(f"Foram digitados {tot} números")
print(f"Lista Decrescente {sorted(num, reverse = True)}")
if 5 in num:
    print(f"O número 5 está na lista ")
else:
    print("O número 5 NÃO está na lista!")
print("Fim do Programa")