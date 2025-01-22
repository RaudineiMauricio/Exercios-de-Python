#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO N INTEIRO QUALQUER E MOSTRE NA TELA
#OS N PRIMEIROS ELEMENTOS DE UMA SEQUÊNCIA DE Fibonacci. EXEMPLO
#0-1-1-2-3-5-8
# Imprime uma linha de 30 traços
print('-' * 30) 

# Imprime o título "SEQUÊNCIA DE FIBONACCI"
print("SEQUÊNCIA DE FIBONACCI") 

# Imprime outra linha de 30 traços
print('-' * 30) 

# Solicita ao usuário que digite um número e converte a entrada para um inteiro
numero = int(input("Digite um número: ")) 

# Inicializa os dois primeiros números da sequência de Fibonacci
t1 = 0  # Primeiro número da sequência
t2 = 1  # Segundo número da sequência

# Imprime os dois primeiros números da sequência
print(f"{t1} -> {t2}", end="") 

# Inicializa um contador a partir do terceiro número
cont = 3 

# Enquanto o contador for menor ou igual ao número digitado pelo usuário
while cont <= numero: 
    # Calcula o próximo número da sequência
    t3 = t1 + t2 
    
    # Imprime o próximo número da sequência
    print(f" -> {t3}", end="") 
    
    # Atualiza os valores de t1 e t2 para os próximos números
    t1 = t2 
    t2 = t3 
    
    # Incrementa o contador
    cont += 1 

# Imprime "FIM" ao final da sequência
print(" -> FIM ")