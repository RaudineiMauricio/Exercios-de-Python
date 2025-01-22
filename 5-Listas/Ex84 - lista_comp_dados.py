# Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista.
# No final, mostre:
#  A) Quantas pessoas foram cadastradas.
#  B) Uma listagem com as pessoas mais pesadas.
#  C) Uma listagem com as pessoas mais leves.

# Criação de listas vazias para armazenar dados temporários e a lista principal com as informações.
temp = []  
princ = []  

# Inicialização das variáveis para o maior e menor peso. Inicialmente, eles são definidos como 0.
maior = menor = 0  
tot = 0  # Contador para o número total de pessoas cadastradas.

# Início de um laço infinito, que só será interrompido quando o usuário decidir.
while True:
    # Adiciona o nome da pessoa na lista 'temp' (como string) e o peso na mesma lista (como inteiro).
    temp.append(str(input("Nome: ")))  # Solicita o nome da pessoa.
    temp.append(int(input("Peso: ")))  # Solicita o peso da pessoa (em kg).

    tot += 1  # Aumenta o contador de pessoas cadastradas.

    # Se esta for a primeira pessoa cadastrada (len(princ) == 0), define o maior e menor peso como o peso dessa pessoa.
    if len(princ) == 0:
        maior = menor = temp[1]  # Define o maior e menor peso como o peso da primeira pessoa cadastrada.
    else:
        # Caso contrário, verifica se o peso da pessoa atual é maior ou menor que os pesos armazenados.
        if temp[1] > maior:
            maior = temp[1]  # Atualiza o maior peso.
        if temp[1] < menor:
            menor = temp[1]  # Atualiza o menor peso.

    # Adiciona a pessoa (nome e peso) à lista principal 'princ'.
    princ.append(temp[:])

    # Limpa a lista temporária para a próxima iteração.
    temp.clear()
    
    # Solicita ao usuário se deseja continuar cadastrando pessoas.
    res = " "
    while res not in "SN":  # Repete até o usuário digitar 'S' ou 'N'.
        res = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    
    # Se o usuário digitar 'N', o loop é interrompido.
    if res == "N":
        break

# Impressão de um separador visual.
print("-=" * 30)

# Exibe o número total de pessoas cadastradas.
print(f"O total de pessoas cadastradas foi {tot}")

# Exibe o maior peso encontrado e o nome das pessoas com esse peso.
print(f"O Maior peso foi de {maior}Kg. Peso de ", end="")
for p in princ:  # Percorre a lista de pessoas.
    if p[1] == maior:  # Se o peso da pessoa for igual ao maior peso.
        print(f"[{p[0]}] ", end="")  # Exibe o nome da pessoa com maior peso.
print()  # Quebra de linha após exibir os nomes.

# Exibe o menor peso encontrado e o nome das pessoas com esse peso.
print(f"O menor peso foi de {menor}Kg. Peso de ", end="")
for p in princ:  # Percorre a lista de pessoas.
    if p[1] == menor:  # Se o peso da pessoa for igual ao menor peso.
        print(f"[{p[0]}] ", end="")  # Exibe o nome da pessoa com menor peso.
print()  # Quebra de linha após exibir os nomes.
