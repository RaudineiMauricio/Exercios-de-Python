#AS TUPLAS SÃO IMUTÁVEIS - VOCE NÃO CONSEGUE MUDADE UMA TUPLA, PARA MUDAR VOCE TEM QUE PARAR O PROGRAMA E MUDAR A TUPLA.

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #junta as duas tuplas, a e b
print(len(c)) #mostra o tamanho da tupla
print(c.count) #para contar quantas vezes aparece um valor
print(c.index[4]) #para mostrar a posição pelo indice

pessoa = ("Gustavo", 39, "M", 99.88) #pode ter dados diferentes na tupla
#del(pessoa) #USADO APAGA A TUPLA

lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")

print(sorted(lanche)) #exibe em ordem 


#sem precisar de posição
for comida in lanche:
    print(f"Eu vou comer {comida}")

#se for precisar de posição

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")

#se precisar de posição
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")
print("Comi pra caramba!")