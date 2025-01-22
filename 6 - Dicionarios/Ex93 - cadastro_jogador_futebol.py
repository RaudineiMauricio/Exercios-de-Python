# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
partidas = []
jogador["nome"] = str(input("Nome do jogador: "))
total = int(input(f"Números de partidas que {jogador["nome"]} jogou? "))
for c in range(0, total):
    partidas.append(int(input(F"Quantos gols na partida {c + 1}? ")))
jogador["gols"] = partidas[:]
jogador["total"] = sum(partidas)
print("-=" * 30)
print(jogador)
print("-=" * 30)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("-=" * 30)
print(f"O jogador {jogador["nome"]} jogou {len(jogador["gols"])} Partidas")
for i, v in enumerate(jogador["gols"]):
    print(f"   => Na partida {i + 1}, fez {v} Gols")
print(f"Foi um total de {jogador["total"]} gols")