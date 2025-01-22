# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.

# Criação de uma lista vazia chamada 'ficha' para armazenar os dados dos alunos
ficha = []

# Início do loop principal que vai pedir as informações dos alunos
while True:
    # Solicita o nome do aluno
    nome = str(input("Nome: "))
    
    # Solicita a primeira nota do aluno e converte para float
    nota1 = float(input("Nota 1: "))
    
    # Solicita a segunda nota do aluno e converte para float
    nota2 = float(input("Nota 2: "))
    
    # Calcula a média das duas notas
    media = (nota1 + nota2) / 2
    
    # Adiciona os dados do aluno (nome, lista com as duas notas e média) à lista 'ficha'
    ficha.append([nome, [nota1, nota2], media])

    # Variável 'resp' que vai armazenar a resposta do usuário sobre continuar ou não
    resp = " "
    
    # Loop para garantir que a resposta seja apenas 'S' ou 'N'
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    
    # Se a resposta for 'N', encerra o loop principal
    if resp == "N":
        break

# Exibe uma linha de separação e um cabeçalho com os títulos das colunas
print("-=" * 30)
print(f"{'No.':<4}{'NOME':<10}{'MEDIA':>8}")
print("-" * 26)

# Laço para exibir todos os alunos e suas respectivas médias
for i, a in enumerate(ficha):
    # Exibe o número do aluno, nome e a média formatada
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")

# Início de um novo loop para o usuário consultar as notas de um aluno específico
while True:
    print("-" * 30)
    
    # Solicita ao usuário que informe o número do aluno (ou 999 para encerrar)
    opcao = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    
    # Se o usuário digitar 999, o programa exibe uma mensagem de finalização e sai do loop
    if opcao == 999:
        print("FINALIZANDO...")
        break
    
    # Verifica se o número do aluno digitado é válido (dentro do intervalo da lista)
    if opcao <= len(ficha) - 1:
        # Exibe as notas do aluno selecionado
        print(f"Notas de {ficha[opcao][0]} são {ficha[opcao][1]}")

# Exibe uma mensagem de despedida ao final do programa
print("<<< VOLTE SEMPRE >>>")

