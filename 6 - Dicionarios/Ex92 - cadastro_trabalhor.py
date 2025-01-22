# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime  # Importa a classe 'datetime' do módulo 'datetime', que é usada para lidar com datas e horas.

dados = dict()  # Cria um dicionário vazio chamado 'dados', que será utilizado para armazenar as informações do usuário.

dados["nome"] = str(input("Nome: "))  # Solicita ao usuário que digite seu nome e armazena o valor no dicionário com a chave "nome". A função 'input' recebe a entrada como string.

nasc = int(input("Ano de Nascimento: "))  # Solicita ao usuário o ano de nascimento, converte para inteiro e armazena na variável 'nasc'.

dados["idade"] = datetime.now().year - nasc  # Calcula a idade do usuário subtraindo o ano atual (obtido com 'datetime.now().year') pelo ano de nascimento ('nasc').

dados["ctps"] = int(input("Carteira de Contratação (0 NÃO TEM): "))  # Solicita ao usuário o número da carteira de trabalho (CTPS). Se o usuário não tiver CTPS, ele pode digitar 0.

# Verifica se o usuário possui carteira de trabalho (se 'dados["ctps"]' é diferente de 0):
if dados["ctps"] != 0:  
    dados["contratação"] = int(input("Ano de contratação: "))  # Se o usuário tem CTPS,
    #solicita o ano de contratação e armazena no dicionário com a chave "contratação".
    
    dados["salário"] = float(input("salário: R$"))  # Solicita o salário do usuário, converte para float e armazena no dicionário com a chave "salário".
    
    # Calcula o ano de aposentadoria com base no ano de contratação, somando 35 anos (idade mínima para aposentadoria) e subtraindo o ano atual.
    dados["aposentadoria"] = dados["idade"] + ((dados["contratação"] + 35) - datetime.now().year)

print("-=" * 30)  # Imprime uma linha de separação para melhorar a visualização.

# Percorre os itens do dicionário 'dados' (as chaves e valores) e imprime cada um de forma formatada.
for k, v in dados.items():  
    print(f" - {k} tem o valor {v}")  # Imprime a chave 'k' e seu valor 'v' de forma legível.
