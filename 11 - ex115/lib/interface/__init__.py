def leiaInt(msg):
    """
    Retorna um valor inteiro
    :param msg: recebe o valor digitado pelo usuário
    :try: Tenta fazer se não tiver erro
    :excpet: mostra as mensagens de erro
    """

    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("Erro! Digite um número válido!")
            continue
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuário")
            return 0
        else:
            return n

def linha(tam = 42):
     return "-" * tam


def cabecalho(txt):
     print(linha())
     print(txt.center(42))
     print(linha())

def menu(lista):
     cabecalho("MENU PRINCIPAL")
     c = 1
     for item in lista:
          print(f"{c} - {item}")
          c+=1
     print(linha())
     opc = leiaInt("Sua Opção: ")
     return opc