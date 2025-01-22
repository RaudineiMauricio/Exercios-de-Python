# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

# Cria uma matriz 3x3 inicializada com zeros
matriz = [[0,0,0],[0,0,0],[0,0,0]]

# Inicia um loop para percorrer as linhas da matriz (de 0 a 2)
for l in range(0, 3):
    # Inicia um loop para percorrer as colunas da matriz (de 0 a 2)
    for c in range(0, 3):
        # Solicita ao usuário que insira um valor para a posição [l][c] da matriz
        # O valor digitado é convertido para inteiro e atribuído à célula correspondente na matriz
        matriz[l][c] = int(input(f"Digite um valor para [{l},{c}]: "))

# Imprime uma linha separadora com "-=" repetido 30 vezes para melhorar a visualização
print("-=" * 30)

# Inicia um loop para percorrer as linhas da matriz (de 0 a 2)
for l in range(0, 3):
    # Inicia um loop para percorrer as colunas da matriz (de 0 a 2)
    for c in range(0, 3):
        # Imprime o valor da célula da matriz [l][c] de forma centralizada em um espaço de 5 caracteres
        # O parâmetro `end=""` impede que o `print()` adicione uma nova linha, ou seja, os valores são impressos na mesma linha
        print(f"[{matriz[l][c]:^5}]", end="")
    # Após cada linha da matriz, o comando `print()` sem argumentos cria uma nova linha
    print()

