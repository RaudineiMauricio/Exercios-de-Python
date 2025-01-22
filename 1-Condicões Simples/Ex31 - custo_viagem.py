#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM.
#CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA VIAGENS DE ATÉ 200KM E R$0,45 PARA VIAGENS MAIS LONGAS

#PEGA O A DISTANCIA DA VIAGEM
distancia_da_viagem = float(input("Quantos KM de distância da sua viagem: "))
print(f"Voce está preste a começar uma viagem de {distancia_da_viagem}km")

#BLOCO PARA CALCULAR O VALOR DA PASSAGEM BASEADO NA DISTANCIA DA VIAGEM
if distancia_da_viagem <= 200:
    preco = distancia_da_viagem * 0.5
else:
    preco =  distancia_da_viagem * 0.45
print(f"E o preço da sua passagem será de R${preco:.2f}") #FORMATAÇÃO DAS CASAS DECIMAIS 

