#Faça um programa que tenha uma função chamada área(),
#que receba as dimensões de um terreno retangular (largura e comprimento)
#e mostre a área do terreno.

def area(largura, comprimento):
    a = largura * comprimento
    print(f"A área de um terreno {largura} x {comprimento} é de {a}²")


#programa principal deixar sempre duas linhas de espaço
print("  CONTROLE DE TERRENO")
print("-=" * 20)
l = float(input("LARGURA (M): "))
C = float(input("COMPRIMENTO (M): "))
area(l, C)



