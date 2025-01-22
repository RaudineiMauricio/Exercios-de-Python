#Faça um programa que tenha uma função chamada ficha()
#que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador,
#mesmo que algum dado não tenha sido informado corretamente.
def ficha(jog ="<desconhecido>", gol=0):  # Define a função 'ficha' com dois parâmetros: 'jog' (com valor padrão "<desconhecido>") e 'gol' (com valor padrão 0).
    print(f"O jogador {jog} fez {gol} no campeoanto")  # Exibe uma mensagem com o nome do jogador e o número de gols no campeonato.


# PROGRAMA PRINCIPAL
n = str(input("Nome do jogador: "))  # Solicita ao usuário que insira o nome do jogador e armazena na variável 'n'.
g = str(input("Gol(s): "))  # Solicita ao usuário que insira o número de gols e armazena como string na variável 'g'.

if g.isnumeric():  # Verifica se o valor inserido em 'g' é numérico.
    g = int(g)  # Converte 'g' para inteiro, caso seja numérico.
else:
    g = 0  # Caso contrário, atribui 0 à variável 'g'.

if n.strip() == "":  # Verifica se o valor de 'n' é uma string vazia ou contém apenas espaços.
    ficha(gol=g)  # Chama a função 'ficha' apenas com o número de gols, usando o valor padrão para 'jog'.
else:
    ficha(n, g)  # Chama a função 'ficha' com os valores fornecidos para 'jog' (nome) e 'gol' (gols).

