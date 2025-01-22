# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
# Inicializando as variáveis:
# 'somarPar' será usada para armazenar a soma dos números pares na matriz.
# 'maior' será usada para armazenar o maior valor da segunda coluna.
# 'somarColuna' será usada para armazenar a soma dos valores da terceira coluna.
somarPar = maior = somarColuna = 0

# Inicializando uma matriz 3x3 com todos os elementos igual a 0.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Preenchendo a matriz com valores fornecidos pelo usuário.
for l in range(0, 3):  # Laço para percorrer as linhas (0 a 2)
    for c in range(0, 3):  # Laço para percorrer as colunas (0 a 2)
        # Pede ao usuário para digitar um valor para cada posição da matriz.
        matriz[l][c] = int(input(f"Digite um valor para [{l},{c}]: "))

# Imprime uma linha de separação visual.
print("-=" * 30)

# Exibe a matriz preenchida.
for l in range(0, 3):  # Laço para percorrer as linhas (0 a 2)
    for c in range(0, 3):  # Laço para percorrer as colunas (0 a 2)
        # Exibe cada valor da matriz, centralizado e com largura de 5 caracteres.
        print(f"[{matriz[l][c]:^5}]", end="")
        
        # Verifica se o valor na posição [l][c] é par.
        if matriz[l][c] % 2 == 0:
            # Se for par, adiciona esse valor à variável 'somarPar'.
            somarPar += matriz[l][c]
    
    # Quebra a linha após cada linha da matriz.
    print()

# Imprime outra linha de separação visual.
print("-=" * 30)

# Exibe o valor da soma dos números pares.
print(f"A soma dos valores pares é {somarPar}")

# Calcula a soma dos valores da terceira coluna (índice 2).
for l in range(0, 3):  # Laço para percorrer as linhas (0 a 2)
    # Adiciona os valores da terceira coluna (índice 2) à variável 'somarColuna'.
    somarColuna += matriz[l][2]

# Exibe a soma dos valores da terceira coluna.
print(f"A Soma dos valores da terceira coluna é {somarColuna}")

# Encontra o maior valor da segunda coluna (índice 1).
for c in range(0, 3):  # Laço para percorrer as colunas (0 a 2)
    if c == 0:
        # Inicializa a variável 'maior' com o valor da primeira linha da segunda coluna.
        maior = matriz[1][c]
    # Compara o valor da segunda coluna (índice 1) com o valor atual de 'maior'.
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

# Exibe o maior valor encontrado na segunda coluna.
print(f"O maior valor da segunda coluna é {maior}")

