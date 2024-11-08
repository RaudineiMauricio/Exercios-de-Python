#CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO.
#NO INICIO, PERGUNTE AO USUÁRIO QUAL SERÁ O VALOR A SER SACADO (NÚMERO INTEIRO)
#E O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES. OBS:
#CONSIDERE QUE O CAIxA POSSUI CÉLULAS DE R$50, R$20, R$10, E R$1

# Imprime uma linha de 40 caracteres '-', que serve para criar uma borda visual
print("-" * 40)

# Imprime a mensagem ' CAIXA ELETRÔNICO ' centralizada em uma linha de 40 caracteres, com o símbolo '=' nas extremidades
print(f"{' CAIXA ELETRÔNICO ':=^40}")

# Imprime outra linha de 40 caracteres '-', para fechar a borda
print("-" * 40)

# Solicita ao usuário que informe o valor que deseja sacar, convertendo a entrada para um inteiro
valor = int(input("Que valor voce quer sacar? R$"))

# Inicializa a variável 'total' com o valor solicitado pelo usuário
total = valor

# Inicializa a variável 'cedula' com o valor da cédula mais alta disponível (R$ 50)
cedula = 50

# Inicializa o contador de cédulas de cada valor que será retirado
total_cedula = 0

# Loop principal que continuará enquanto houver saldo a ser sacado
while True:
    # Verifica se o total restante é maior ou igual ao valor da cédula
    if total >= cedula:
        # Se sim, subtrai o valor da cédula do total
        total -= cedula
        # Incrementa o contador de cédulas retiradas desse valor
        total_cedula += 1
    else:
        # Se já foram retiradas cédulas desse valor, imprime o total de cédulas retiradas
        if total_cedula > 0:
            print(f"Total de {total_cedula} cédulas de R${cedula}")
        
        # Após retirar as cédulas do valor atual, altera o valor da cédula para o próximo menor
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        
        # Reseta o contador de cédulas para o próximo valor
        total_cedula = 0
        
        # Se o total restante for zero, significa que o saque foi completado, então sai do loop
        if total == 0:
            break

# Imprime uma linha de 30 caracteres '=', indicando o fim do processo
print("=" * 30)

# Exibe uma mensagem final de despedida ao usuário
print("Volte Sempre ao Banco dos Lisos!!")
