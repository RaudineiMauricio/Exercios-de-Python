#DESELVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULE SEU
#INDICE DE MASSA CORPORAL (IMC) E MOSTRE  SEU STATUS, DE ACORDO COM A TABELA ABAIXO
# - IMC ABAIXO DE 18,5: ABAIXO DO PESO
# - ENTRE 18,5 E 25: PESO IDEAL
# - 25 ATÉ 30: SOBREPESO
# - 30 ATÉ 40: OBESIDADE
# - ACIMA DE 40: OBESIDADE MÓRBIDA

peso = float(input("Digite seu Peso: "))
altura = float(input("Digite sua Altura: "))
imc = peso / (altura **2)

if imc < 18.5:
    print(f"Seu IMC é {imc:.2f} e voce está Abaixo do peso")
elif imc <= 25:
    print(f"Seu IMC é {imc:.2f} e voce está no peso Ideal")
elif imc <=30:
    print(f"Seu IMC é {imc:.2f} e voce está com Sobrepeso")
elif imc <=40:
    print(f"Seu IMC é {imc:.2f} e voce está com Obesidade")
else:
    print("Voce Está com Obsidade Mórbida")