# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

# Gerando os resultados dos jogadores
jogo = {
    "jogador1": randint(1, 6),
    "jogador2": randint(1, 6),
    "jogador3": randint(1, 6),
    "jogador4": randint(1, 6)
}

# Lista para armazenar o ranking (inicialmente vazia)
ranking = []

# Exibe os valores sorteados para cada jogador
print("Valores Sorteados: ")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)  # Pausa de 1 segundo entre cada exibição

# Ordenando os jogadores com base no valor sorteado (do maior para o menor)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

# Exibe o título do ranking
print("-=" * 30)
print("  == RANKING DOS JOGADORES   == ")

# Exibe o ranking final
for i, v in enumerate(ranking):
    print(f"  {i + 1}* lugar: {v[0]} com {v[1]}")
    sleep(1)

