#DESENVOLVA UM PROGRAMA QUE LEIA 6 NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELAS QUE FOREM PARES.
#SE O VALOR VALOR DIGITADO FOR IMPAR, DESCONSIDERO-O.

soma = 0  # Inicializa a variável 'soma' que irá armazenar a soma dos números pares
cont = 0  # Inicializa a variável 'cont' que irá contar quantos números pares foram informados
# Inicia um loop que irá iterar 6 vezes (de 1 a 6)
for c in range(1, 7):
    num = int(input(f"Digite o {c}° número: "))  # Pede ao usuário para digitar um número e converte para inteiro
    if num % 2 == 0:  # Verifica se o número é par
        soma += num  # Se for par, adiciona o número à soma
        cont += 1    # Incrementa o contador de números pares

# Após o loop, imprime quantos números pares foram informados e a soma desses números
print(f"Voce inforou {cont} números PARES e a soma foi {soma}")

