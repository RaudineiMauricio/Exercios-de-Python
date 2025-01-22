#DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO E GUARDE-OS
#EM UMA TUPLA. NO FINAL, MOSTRE:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

num = (int(input("Digite um valor: ")),
       int(input("Digite outro valor: ")),
       int(input("Digite mais um valor: ")),
       int(input("Digite o Último valor: ")))

print(f"Voce digitou os valores {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3)+1}")
else:
    print("O valor 3 não foi digitado em nenhuma Posição")
print("Os valores pares digitados foram ", end="")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")
