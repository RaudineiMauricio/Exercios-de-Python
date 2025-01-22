#  Crie um programa que leia nome, sexo e idade de várias pessoas,
#  guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#  No final, mostre:
#  A) Quantas pessoas foram cadastradas
#  B) A média de idade
#  C) Uma lista com as mulheres
#  D) Uma lista de pessoas com idade acima da média
galera = list()  # Cria uma lista vazia chamada 'galera' para armazenar os dados das pessoas.
pessoa = dict()  # Cria um dicionário vazio chamado 'pessoa', que será usado para armazenar as informações de cada pessoa.
soma = media = 0  # Inicializa as variáveis 'soma' e 'media' com o valor 0. 'soma' acumula as idades e 'media' será a média das idades.

# Laço principal que permite o cadastro de várias pessoas até que o usuário decida parar.
while True:
    pessoa.clear()  # Limpa o dicionário 'pessoa' para garantir que ele seja reutilizado sem dados antigos.
    
    pessoa["nome"] = str(input("Nome: "))  # Solicita o nome da pessoa e armazena no dicionário 'pessoa' com a chave "nome".
    
    # Laço para garantir que o sexo seja informado corretamente (apenas 'M' ou 'F').
    while True:
        pessoa["sexo"] = str(input("Sexo: [M/F] ")).upper()[0]  # Solicita o sexo e converte para maiúsculo, pegando apenas a primeira letra.
        if pessoa["sexo"] in "MF":  # Verifica se a entrada está em 'M' ou 'F'.
            break  # Sai do laço se a entrada for válida.
        print("ERRO! Por favor, digite apenas M OU F.")  # Mensagem de erro caso o sexo informado seja inválido.
    
    pessoa["idade"] = int(input("idade: "))  # Solicita a idade e converte para inteiro, armazenando no dicionário 'pessoa'.
    
    soma += pessoa["idade"]  # Soma a idade da pessoa à variável 'soma' (acumulador das idades).
    
    galera.append(pessoa.copy())  # Adiciona uma cópia do dicionário 'pessoa' à lista 'galera' (armazenamento das pessoas cadastradas).
    
    # Laço para perguntar se o usuário deseja continuar cadastrando mais pessoas.
    while True:
        resp = str(input("Deseja continuar? [S/N]")).upper()[0]  # Pergunta se o usuário deseja continuar e pega apenas a primeira letra.
        if resp in "SN":  # Verifica se a resposta é válida ('S' ou 'N').
            break  # Sai do laço se a resposta for válida.
        print("ERRO! Responda apenas S OU N.")  # Mensagem de erro caso a resposta não seja válida.
    
    if resp == "N":  # Se a resposta for 'N', significa que o usuário não deseja continuar.
        break  # Sai do laço principal e termina o cadastro.

# Exibe um cabeçalho para separar a saída
print("-=" * 30)

# A) Exibe o número total de pessoas cadastradas.
print(f"A) Ao todo temos {len(galera)} pessoas cadastradas.")

# Calcula a média das idades e exibe.
media = soma / len(galera)  # A média de idades é calculada dividindo a soma das idades pelo número de pessoas.
print(f"B) A média de idade [e de {media:5.2f}] anos.")  # Exibe a média com 2 casas decimais.

# C) Exibe o nome das mulheres cadastradas.
print(f"C) As mulhes cadastradas foram ", end="")  # Inicia a impressão das mulheres.
for p in galera:  # Percorre a lista 'galera' que contém os dicionários das pessoas.
    if p["sexo"] in "Ff":  # Verifica se o sexo é feminino ('F' ou 'f').
        print(f"{p['nome']} ", end="")  # Imprime o nome da mulher encontrada.
print()  # Quebra de linha após imprimir os nomes das mulheres.

# D) Exibe a lista de pessoas que estão acima da média de idade.
print("D) Lista das pessoas que estão acima da média: ", )
for p in galera:  # Percorre novamente a lista 'galera'.
    if p["idade"] >= media:  # Verifica se a idade da pessoa é maior ou igual à média.
        print("   ", end="")  # Imprime um espaçamento antes de mostrar os detalhes da pessoa.
        for k, v in p.items():  # Percorre os itens do dicionário 'pessoa'.
            print(f"{k} = {v}; ", end="")  # Exibe a chave e o valor de cada item no formato 'chave = valor'.
        print()  # Quebra de linha após exibir todos os detalhes da pessoa.

# Exibe a mensagem de encerramento do programa.
print("<<< ENCERRADO >>>")

