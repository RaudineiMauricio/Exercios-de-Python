# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
# Importante: use cores.
from time import sleep  # Importa a função sleep, que permite pausar a execução do programa por um determinado período.

# Define uma tupla de strings contendo códigos de escape ANSI para adicionar cores ao terminal.
c = ('\033[m',         # 0 - sem cores (reset)
     '\033[0;30;41m',  # 1 - VERMELHO (fundo vermelho, texto preto)
     '\033[0;30;42m',  # 3 - VERDE (fundo verde, texto preto)
     '\033[0;30;43m',  # 4 - AMARELO (fundo amarelo, texto preto)
     '\033[0;30;44m',  # 5 - AZUL (fundo azul, texto preto)
     '\033[0;30;45m',  # 6 - ROXO (fundo roxo, texto preto)
     '\033[7;30m'      # 7 - BRANCO (fundo branco invertido, texto preto)
     )

# Função que exibe o manual de ajuda do Python para um comando/biblioteca.
def ajuda(com):
    """_summary_

    Parameters
    ----------
    com : _type_
        _description_
    """    
    
    # Exibe um título indicando qual comando está sendo acessado.
    titulo(f"Acessando o manual do comando \"{com}\"", 4)
    # Define a cor de fundo como roxo antes de exibir o conteúdo do `help`.
    print(c[6], end="")
    help(com)  # Exibe o manual da função/biblioteca passada como parâmetro.
    # Reseta as cores do terminal.
    print(c[0], end="")
    sleep(2)  # Aguarda 2 segundos antes de continuar.

# Função que exibe um título formatado com uma mensagem e uma cor.
def titulo(msg, cor=0):
    """_summary_

    Parameters
    ----------
    msg : _type_
        _description_
    cor : int, optional
        _description_, by default 0
    """    

    
    tam = len(msg) + 4  # Calcula o tamanho do título (mensagem + margens).
    print(c[cor], end="")  # Define a cor de fundo especificada.
    print("~" * tam)       # Imprime uma linha de separação acima da mensagem.
    print(f"  {msg}")      # Exibe a mensagem com margens de espaço.
    print("~" * tam)       # Imprime uma linha de separação abaixo da mensagem.
    print(c[0], end="")    # Reseta as cores do terminal.
    sleep(1)  # Aguarda 1 segundo antes de continuar.

# PROGRAMA PRINCIPAL

comando = ""  # Inicializa a variável que armazenará o comando digitado pelo usuário.
while True:
    # Exibe o título inicial do programa.
    titulo("SISTEMA DE AJUDA PyHELP", 2)
    comando = str(input("Função ou Biblioteca > "))  # Solicita ao usuário um comando ou biblioteca.
    if comando.upper() == "FIM":  # Verifica se o usuário digitou "FIM" para encerrar o programa.
        break  # Sai do loop principal.
    else:
        ajuda(comando)  # Chama a função de ajuda para exibir o manual do comando digitado.

# Exibe uma mensagem de despedida quando o programa termina.
titulo("ATÉ LOGO!", 1)
