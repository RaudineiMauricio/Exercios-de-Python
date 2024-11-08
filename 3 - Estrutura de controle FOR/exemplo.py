s = 0  # Inicializa a variável 's' com 0, que irá armazenar a soma dos valores.

# Inicia um loop que irá repetir 3 vezes (c = 0, 1, 2).
for c in range(0, 3):
    n = int(input("Digite um valor: "))  # Solicita ao usuário que digite um valor, converte para inteiro e armazena na variável 'n'.
    s += n  # Adiciona o valor de 'n' à variável 's', acumulando a soma.

# Exibe o resultado final, mostrando a soma de todos os valores digitados.
print(f"O somatório de todos os valores foi {s}")
