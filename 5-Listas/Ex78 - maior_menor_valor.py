#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

listanum = []  # Cria uma lista vazia para armazenar os números digitados.
maior = 0  # Inicializa a variável `maior` que será usada para armazenar o maior valor.
menor = 0  # Inicializa a variável `menor` que será usada para armazenar o menor valor.

# Laço para solicitar ao usuário 5 números.
for c in range(0, 5):  
    # Adiciona um número digitado pelo usuário na lista.
    listanum.append(int(input(f"Digite um valor para a posição {c}: ")))  
    if c == 0:  # Na primeira iteração, define o primeiro número como maior e menor.
        maior = menor = listanum[c]
    else:
        # Atualiza o valor de `maior` se o número atual for maior.
        if listanum[c] > maior:  
            maior = listanum[c]
        # Atualiza o valor de `menor` se o número atual for menor.
        if listanum[c] < menor:  
            menor = listanum[c]

print("=-" * 30)  # Exibe uma linha de separação.
print(f"Você digitou os valores {listanum}")  # Mostra todos os números digitados.

# Mostra o maior valor e as posições onde ele aparece.
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for i, v in enumerate(listanum):  # Enumera os índices e valores da lista.
    if v == maior:  # Verifica se o valor atual é igual ao maior.
        print(f"{i}...", end="")  # Imprime a posição do maior valor.
print()  # Pula uma linha.

# Mostra o menor valor e as posições onde ele aparece.
print(f"O menor valor digitado foi {menor} nas posições ", end="")
for i, v in enumerate(listanum):  # Enumera os índices e valores da lista.
    if v == menor:  # Verifica se o valor atual é igual ao menor.
        print(f"{i}...", end="")  # Imprime a posição do menor valor.
print()  # Finaliza o programa com uma linha em branco.
