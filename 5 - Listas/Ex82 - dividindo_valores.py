# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []
while True:
    num = int(input("Digite um valor: "))
    lista.append(num)

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print("-=" * 30)
print(f"sua Lista {lista}")
print(f"Lista com números pares {par}")
print(f"Lista com números impares {impar}")