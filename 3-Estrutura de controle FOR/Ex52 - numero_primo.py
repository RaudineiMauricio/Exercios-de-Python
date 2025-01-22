#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO.

num = int(input("Digite um Número: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[33m", end=" ")
        tot += 1
    else:
        print("\033[31m", end=" ")
    print(f"{c}", end=" ")
print(f"\n\033[mO número {num} foi divisivel {tot} vezes")
if tot == 2:
    print("É por isso que ele é PRIMO")
else:
    print("É por isso que ele NÃO É PRIMO")

        
   

