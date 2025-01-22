#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.


# Criação de uma tupla chamada 'produtos', que contém os nomes dos produtos e seus respectivos preços.
produtos = ("ROSA MOSQUETA", 65.90, "ALECRIM", 200.90, "SEMENTE DE UVA", 119.90,
            "OJON", 76.90, "ABACATE", 150.90, "ALOE VERA", 46.90,
            "AMÊNDOAS DOCE", 47.90, "ARGAN", 66.90, "JOJOBA", 48.90,
            "MAMONA", 52.90)

# Imprime uma linha de 40 caracteres com o símbolo de traço '-', para separar a listagem.
print("-" * 40)

# Exibe o título "LISTAGEM DE PREÇOS" centralizado com 40 caracteres de largura.
# O operador ^ dentro de f-strings centraliza o texto.
print(f"{"LISTAGEM DE PREÇOS":^40}")  # CENTRALIZA O "LISTAGEM DE PREÇOS"

# Imprime outra linha de 40 caracteres com traços '-', para separar o título da listagem.
print("-" * 40)

# Inicia um laço 'for' que vai iterar por cada elemento da tupla 'produtos'.
# O 'range(0, len(produtos))' faz o laço percorrer de 0 até o tamanho total da tupla.
for pos in range(0, len(produtos)): 
    # Verifica se a posição (índice) é par, ou seja, se o produto está na primeira posição da dupla "produto-preço".
    if pos % 2 == 0:  # Verifica se a posição é par (nomes dos produtos estão nas posições pares)
        # Imprime o nome do produto, alinhando à esquerda com 30 caracteres. O 'end=""' evita quebrar a linha.
        print(f"{produtos[pos]:.<30}", end="")  # Formatação: nome do produto alinhado à esquerda
    else:
        # Imprime o preço, alinhando à direita com 8 caracteres e 2 casas decimais.
        print(f"R${produtos[pos]:>8.2f}")  # Formatação: preço alinhado à direita com 2 casas decimais
print("-" * 40)

