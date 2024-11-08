n = 1  # Inicializa a variável n com um valor diferente de 0 para entrar no loop.
par = impar = 0  # Inicializa contadores para números pares e ímpares.

while n != 0:  # O loop continua enquanto n for diferente de 0.
    n = int(input("Digite um valor: "))  # Pede ao usuário para digitar um número e converte para inteiro.
    if n % 2 == 0:  # Verifica se o número é par (divisível por 2).
        par += 1  # Se for par, incrementa o contador de pares.
    else:
        impar += 1  # Se não for par (portanto é ímpar), incrementa o contador de ímpares.

# Após o loop, exibe a quantidade de números pares e ímpares digitados.
print(f"Você digitou {par} números pares e {impar} números ímpares!")
