from interface import *
from time import sleep
from arquivo import *

arq = "cursoemvideo.txt"

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(["Ver Pessoas Cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema" ])
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo!
        ler_arquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa.
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho("Saindo do Sistema...Até Logo!")
        break
    else:
        print("\33[31mERRO! Digite uma opção válida!\33[m")
    sleep(2)