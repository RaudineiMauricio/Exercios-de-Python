#  Crie um programa onde o usuário possa digitar sete valores numéricos
#  e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#  No final, mostre os valores pares e ímpares em ordem crescente.
 
# Inicializa a lista 'num' com duas sublistas vazias, uma para números pares e outra para números ímpares.
num = [[], []]

# Variável que irá armazenar os valores digitados pelo usuário.
valor = 0

# Laço de repetição que vai de 1 até 7 (inclusive), totalizando 7 iterações.
for n in range(1, 8):
    # Solicita ao usuário que digite um valor inteiro e armazena esse valor na variável 'valor'.
    valor = int(input(f"Digite o {n}* valor: "))

    # Adiciona o valor à lista 'num'. Porém, isso adiciona o valor na lista principal, não nas sublistas.
    num.append(valor)

    # Verifica se o valor digitado é par (divisível por 2).
    if valor % 2 == 0:
        # Se o número for par, adiciona ele na primeira sublista de 'num' (índice 0).
        num[0].append(valor)
    else:
        # Se o número for ímpar, adiciona ele na segunda sublista de 'num' (índice 1).
        num[1].append(valor)

# Exibe uma linha de separação para melhorar a organização visual da saída.
print("-=" * 30)

# Ordena a lista de números pares (sublista de índice 0) em ordem crescente.
num[0].sort()

# Ordena a lista de números ímpares (sublista de índice 1) em ordem crescente.
num[1].sort()

# Exibe a lista de números pares, ordenada em ordem crescente, usando a função 'sorted' para garantir a ordenação.
print(f"Lista com numeros pares em ordem Crescente {sorted(num[0])}")

# Exibe a lista de números ímpares, ordenada em ordem crescente, usando a função 'sorted' para garantir a ordenação.
print(f"Lista com os valores ímpares em ordem Crescente{sorted(num[1])}")

