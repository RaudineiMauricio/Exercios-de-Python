#CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALÍNDROMO,
#DESCONSIDERANDO OS ESPAÇOS. EXEMPLOS DE PALÍNDROMOS.
#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

#LER A FRASE USANDO FOR
# Lê uma frase do usuário, removendo espaços no início e no fim, e convertendo tudo para maiúsculas
'''frase = str(input("Digite uma Frase: ")).strip().upper() 

# Divide a frase em uma lista de palavras, separando por espaços
palavras = frase.split() 

# Junta as palavras em uma única string, removendo os espaços
junto = "".join(palavras) 

# Inicializa uma string vazia para armazenar o inverso da string
inverso = ""

# Lógica para inverter a string 'junto'
# Loop que percorre os índices da string de trás para frente
for letra in range(len(junto)-1, -1, -1): 
    inverso += junto[letra]  # Adiciona cada letra ao 'inverso'

# Compara a string original (junto) com a invertida (inverso)
if inverso == junto:
    # Se forem iguais, significa que é um palíndromo
    print(f"O inverso de {junto} é {inverso}")
    print("Temos um Palíndromo")
else:
    # Se não forem iguais, a frase não é um palíndromo
    print("A frase digitada não é um Palíndromo")
'''

#SEM FOR
# Lê uma frase do usuário, removendo espaços no início e no fim, e convertendo para maiúsculas
frase = str(input("Digite uma Frase: ")).strip().upper() 

# Divide a frase em uma lista de palavras
palavras = frase.split() 

# Junta as palavras em uma única string, sem espaços
junto = "".join(palavras) 

# Inverte a string usando fatiamento
inverso = junto[::-1]

# Exibe o inverso da string
print(f"O inverso de {junto} é {inverso}")

# Compara a string original (junto) com a invertida (inverso)
if inverso == junto:
    print(f"Temos um Palíndromo")  # Se forem iguais, é um palíndromo
else:
    print("A frase digitada não é um Palíndromo")  # Se não, não é um palíndromo
