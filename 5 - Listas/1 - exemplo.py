''''num = [2,5,9,1]
#num[2] = 3
num.append(7) #adicionar numero a lista
num.sort(reverse = True) #ordem decrescente
num.insert(2, 2) #insere o 0 na posicão 2 
num.pop(2) #Exclui na posicão 2
num.remove(2) #remove o primeiro elemento 2, procura do inicio da lista e elimina,
#ele nao percorre todo o resto da lista, pra isso deve usar um laço
if 5 in num:
    num.remove(5)
else:
    print("Não achei o número 5 ")

print(num)
print(f"Essa liste tem {len(num)}") '''

#OUTROS EXEMPLOS


''''valores = []'''

''''for cont in range(0, 5):
    valores.append(int(input("Digite um valor: "))) 

for c, v in enumerate(valores): #o C é a posição dos valores
    print(f"Na posição {c} Encontrei o valor {v}")

print("Chegei ao final da lista.")

a = [2,3,4,5,7]
b = a[:] #copia de todos os valores de A dentro de B
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")
'''
#PARTE 2

'''teste = list()
teste.append("Gustavo")
teste.append(40)
galera = list()
galera.append(teste[:]) #cria uma copia de teste
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera)
'''

galera = [["joão", 19],["ANA", 33],["Joaquin", 13],["Maria", 45]]
for pessoas in galera:
    print(f"{pessoas[0]} tem {pessoas[1]} anos de idade!!")



galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("idade: ")))
    galera.append(dado[:]) #cria uma cópia de dados
    dado.clear() #limpa a lista de dados

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
    else:
        print(f"{p[0]} é menor de idade.")

print(f"Temos {totmai} maiores e {totmen} menores de idade.")