n1 = float(input("Digite a Primeira nota: "))
n2 = float(input("Digite a Segunda nota: "))

#RECEBENDO A MÉDIA 
media = (n1 + n2) / 2
print(f" A Sua média foi {media:.1f}")

#BLOCO DE CONDIÇÃO SE E SENAO
if media >= 6.0:
    print("Sua Média foi Boa, Parabéns")
else:
    print("Sua Média foi Ruim, Estude Mais!!")

