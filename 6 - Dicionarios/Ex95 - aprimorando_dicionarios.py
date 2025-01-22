# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

# Inicializando as variáveis
time = []  # Lista para armazenar os jogadores
jogador = {}  # Dicionário temporário para armazenar os dados de um jogador
partidas = []  # Lista para armazenar os gols feitos em cada partida

# Loop principal para registrar os jogadores e suas informações
while True:
    jogador.clear()  # Limpa os dados do jogador anterior, se houver
    jogador["nome"] = input("Nome do jogador: ")  # Pergunta o nome do jogador
    
    # Pergunta quantas partidas o jogador jogou
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    partidas.clear()  # Limpa os gols das partidas do jogador

    # Loop para registrar os gols de cada partida
    for c in range(tot):
        # Pergunta quantos gols o jogador fez em cada partida
        gols = int(input(f"   Quantos gols na partida {c+1}? "))
        partidas.append(gols)

    # Adiciona os gols e o total de gols ao dicionário do jogador
    jogador["gols"] = partidas[:]  # Copia os gols das partidas para o dicionário
    jogador["total"] = sum(partidas)  # Soma os gols para calcular o total de gols

    # Adiciona o jogador à lista de time (com as informações completas)
    time.append(jogador.copy())

    # Pergunta se o usuário quer continuar adicionando jogadores
    while True:
        resp = input("Quer continuar? [S/N] ").strip().upper()  # Pede a resposta para continuar
        if resp in "SN":  # Verifica se a resposta é válida
            break
        print("ERRO! Responda apenas S ou N.")  # Se a resposta for inválida, pede novamente

    if resp == "N":  # Se o usuário responder "N", encerra o loop de adição de jogadores
        break

# Imprime o cabeçalho da tabela de jogadores
print("-=" * 30)
print("cod ", end="")  # Imprime a palavra "cod"
for i in jogador.keys():  # Percorre as chaves do dicionário "jogador"
    print(f"{i:<15}", end="")  # Imprime as chaves com formatação de alinhamento à esquerda
print()  # Pula para a linha seguinte
print("-=" * 30)

# Imprime os dados de todos os jogadores
for k, v in enumerate(time):  # Percorre a lista de jogadores
    print(f"{k:>3} ", end="")  # Imprime o código do jogador (índice na lista)
    for d in v.values():  # Percorre os valores do dicionário do jogador
        print(f"{str(d):<15}", end="")  # Imprime cada valor com formatação de alinhamento à esquerda
    print()  # Pula para a linha seguinte
print("-=" * 40)

# Loop para mostrar os dados detalhados de um jogador específico
while True:
    # Pergunta o código do jogador a ser detalhado
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    
    if busca == 999:  # Se o código for 999, o programa para
        break

    # Verifica se o código do jogador existe na lista
    if busca >= len(time):  
        print(f"ERRO! Não existe jogador com código {busca}!")  # Se não existir, exibe erro
    else:
        # Exibe os dados do jogador solicitado
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}: ")
        for i, g in enumerate(time[busca]["gols"]):  # Mostra os gols do jogador em cada partida
            print(f"   No jogo {i+1} fez {g} gols.")
    print("-" * 40)

# Mensagem final
print("<<<< VOLTE SEMPRE >>>>")
