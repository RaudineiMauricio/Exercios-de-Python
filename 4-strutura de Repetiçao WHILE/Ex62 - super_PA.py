#MELHOE O EXERCICIO 61, PERGUNTANDO OARA O USUÁRIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS.
#O PROGRAMA ENCERRARÁ QUANDO ELE DISSER QUE QUER MOSTRAR 0 TERMOS

# Exibe o título do contador de PA (Progressão Aritmética)
print("CONTADADOR DE PA")  
# Exibe uma linha de separação
print("-=-" * 20)  

# Solicita ao usuário o primeiro termo da PA e converte para inteiro
primeiro = int(input("Digite o Primeiro termo da PA: "))  
# Solicita ao usuário a razão da PA e converte para inteiro
razao = int(input("Digite a Razao da PA: "))  

# Inicializa a variável 'termo' com o primeiro termo da PA
termo = primeiro  
# Inicializa o contador de termos exibidos
cont = 1  
# Inicializa o total de termos exibidos
total = 0  
# Inicializa a variável 'mais' com 10, que representa a quantidade de termos a serem mostrados
mais = 10  

# Enquanto 'mais' for diferente de 0, continua o loop
while mais != 0:  
    # Adiciona a quantidade de termos a serem mostrados ao total
    total = total + mais  
    # Enquanto o contador for menor ou igual ao total de termos
    while cont <= total:  
        # Exibe o termo atual da PA
        print(f"{termo} -> ", end="")  
        # Calcula o próximo termo da PA
        termo += razao  
        # Incrementa o contador
        cont += 1  
    # Solicita ao usuário quantos termos a mais ele deseja mostrar
    mais = int(input("Quantos termos voce quer mostrar a mais? "))  
    # Exibe uma pausa
    print("PAUSA")  

# Exibe a mensagem final com o total de termos mostrados
print(f"Progressao finalizada com {total} termos mostrados!!") 
