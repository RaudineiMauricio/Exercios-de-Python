#FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR()
#QUE RECEBA TRÊS PARÂMETROS: INICIO, FIM E PASSO.
#SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGENS  ATRÁVES DA FUNÇÃO CRIADA:
#A) DE 1 ATÉ 10, DE 1 EM 1
#B) DE 10 ATÉ 0, DE 2 EM 2
#C) UMA CONTAGEM PERSONALIZADA

from time import sleep  # Importa a função sleep do módulo time, que permite adicionar pausas no código.

def contador(i, f, p):  # Define a função 'contador' que recebe três parâmetros: i (início), f (fim), e p (passo).
    if p < 0:  # Verifica se o passo é negativo.
        p *= -1  # Se o passo for negativo, inverte o sinal, tornando-o positivo.
    if p == 0:  # Verifica se o passo é igual a zero.
        p = 1  # Se o passo for zero, define o passo como 1 para evitar um loop infinito.
    print("-=" * 20)  # Imprime uma linha de separação (40 vezes o caractere "-").
    print(f"Contagem de {i} até {f} de {p} em {p}")  # Exibe uma mensagem indicando o início da contagem.
    sleep(2.5)  # Faz uma pausa de 2.5 segundos antes de começar a contagem.

    if i < f:  # Verifica se o valor inicial é menor que o valor final.
        cont = i  # Define a variável 'cont' como o valor inicial.
        while cont <= f:  # Enquanto 'cont' for menor ou igual ao valor final, continua a contagem.
            print(f"{cont} ", end="", flush=True)  # Imprime o valor atual da contagem, sem pular linha.
            sleep(0.5)  # Faz uma pausa de 0.5 segundos entre cada número.
            cont += p  # Incrementa o valor de 'cont' pelo valor do passo.
        print("FIM")  # Após a contagem, imprime "FIM" indicando o término.
    else:  # Caso o valor inicial seja maior que o valor final (contagem regressiva).
        cont = i  # Define a variável 'cont' como o valor inicial.
        while cont >= f:  # Enquanto 'cont' for maior ou igual ao valor final, continua a contagem.
            print(f"{cont} ", end="", flush=True)  # Imprime o valor atual da contagem, sem pular linha.
            sleep(0.5)  # Faz uma pausa de 0.5 segundos entre cada número.
            cont -= p  # Decrementa o valor de 'cont' pelo valor do passo.
        print("FIM")  # Após a contagem, imprime "FIM" indicando o término.


#PROGRAMA PRINCIPAL
contador(1, 10, 1)  # Chama a função 'contador' com os parâmetros 1 (início), 10 (fim) e 1 (passo).
contador(10, 0, 2)  # Chama a função 'contador' com os parâmetros 10 (início), 0 (fim) e 2 (passo).
print("-=" * 20)  # Imprime uma linha de separação.
print("Agora é sua vez de personalizar a contagem!")  # Mensagem pedindo para o usuário personalizar a contagem.
ini = int(input("INICIO:  "))  # Solicita ao usuário o valor inicial da contagem e converte para inteiro.
fim = int(input("FIM:     "))  # Solicita ao usuário o valor final da contagem e converte para inteiro.
pas = int(input("PASSO:   "))  # Solicita ao usuário o valor do passo da contagem e converte para inteiro.
contador(ini, fim, pas)  # Chama a função 'contador' com os valores fornecidos pelo usuário.
