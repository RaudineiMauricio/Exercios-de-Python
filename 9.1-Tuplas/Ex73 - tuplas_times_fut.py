#CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA
#DO CAMPEONATO BRASILEIRO DE FUTEBOL, NA ORDEM DE COLOCAÇÃO. DEPOIS MOSTRE

#A) OS 5 PRIMEIROS TIMES
#B) OS ÚLTIMOS 4 COLOCADOS
#C) TIMES EM ORDEM ALFABÉTICA
#D) EM QUE POSIÇÃO ESTÁ O TIME DA VASCO.

times = ("BOTAFOGO", "PALMEIRAS", "FLAMENGO", "FORTALEZA", "INTERNACIONAL",
         "SÃO PAULO", "CORINTHIANS", "BAHIA", "CRUZEIRO", "VASCO",
         "VITORIA", "ATLÉTICO MINEIRO", "FLUMINENSE", "GRÊMIO", "JUVENTUDE",
         "BRAGANTINO", "ATHLETICO-PR", "CRICIÚMA", "ATLÉTICO-GO", "CUIABÁ")

print(f"Lista de times do Brasileirão 2024 {times}")
print("-=" * 50)
print(f"Os 5 Primeiros colocados são {times[0:5]}")
print("-=" * 50)
print(f"Os 4 últimos colocados são {times[-4:]}")
print("-=" * 50)
print(f"Times em Ordem Alfabética: {sorted(times)}")
print("-=" * 50)
print(f"O VASCO está na posição {times.index("VASCO")+1}")




