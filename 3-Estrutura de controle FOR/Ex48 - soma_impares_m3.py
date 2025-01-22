#FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS QUE SAO MÚLTIPLOS DE TRES,
#E QUE SE ENCONTRAM NO INTERVALO DE 1 A 500.

soma = 0  # Inicializa a variável soma com 0 para armazenar a soma dos números que atendem às condições.
cont = 0  # Inicializa a variável cont com 0 para contar quantos números foram somados.

# Inicia um loop que vai de 1 até 500, pegando apenas os números ímpares (incremento de 2).
for num in range(1, 501, 2):
    # Verifica se o número atual (num) é divisível por 3.
    if num % 3 == 0:
        soma += num  # Se for, adiciona esse número à soma.
        cont += 1    # E incrementa o contador de números somados.

# Após o loop, imprime a soma total e quantos números foram considerados.
print(f"A soma de todos os {cont} valores solicitados é {soma}")
