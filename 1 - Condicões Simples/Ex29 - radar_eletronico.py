#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO
#SE ELE ULTRAPASSAR 80KM/H, MONSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO
#A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE

velocidade = float(input("Qual a velocidade atualdo carro? "))
if velocidade > 80:
    print("MULTADO, Voce Excedeu o limite de velocidade que é de 80km/h")
    multa = (velocidade-80)*7
    print(f"Voce deve pagar uma multa no valor de R${multa}")
print("Dirija com Cuidado!!")


