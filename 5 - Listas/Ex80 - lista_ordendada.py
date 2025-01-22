# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
lista = []  # Inicializa uma lista vazia para armazenar os valores digitados.

# Laço que será executado 5 vezes, para permitir que o usuário insira valores.
for c in range(0, 5):
    n = int(input("Digite um valor: "))  # Solicita ao usuário um valor inteiro.
    
    # Se for o primeiro valor ou se `n` for maior que o último valor da lista.
    if c == 0 or n > lista[-1]:  
        lista.append(n)  # Adiciona o valor ao final da lista.
        print("Adicionado no final da lista...")
    else:
        pos = 0  # Inicializa a variável de posição para começar da posição 0.
        
        # Laço para encontrar a posição correta onde `n` deve ser inserido.
        while pos < len(lista):
            if n <= lista[pos]:  # Se `n` for menor ou igual ao valor atual na lista.
                lista.insert(pos, n)  # Insere `n` na posição encontrada.
                print(f"Adicionado na posição {pos} da lista...")
                break  # Sai do laço assim que o valor for inserido.
            pos += 1  # Incrementa a posição para verificar o próximo índice.

# Imprime uma linha de separação.
print("-=" * 30)

# Exibe os valores digitados na ordem em que foram armazenados na lista.
print(f"Os valores digitados em ordem foram {lista}")

