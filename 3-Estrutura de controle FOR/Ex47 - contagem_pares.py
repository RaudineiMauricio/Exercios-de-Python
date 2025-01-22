#CRIE UM PROGRAMA QUE MOSTRE NA TELA TODOS OS NÚMEROS PARES QUE ESTÃO NO INTERVALO ENTRE 1 E 50.

for cont in range(1, 51):
    if cont % 2 == 0:
        print(cont, end=" ") #end=" " para que a lista de resultados fique na diagonal.
print("FIM DA CONTAGEM DE PARES") 