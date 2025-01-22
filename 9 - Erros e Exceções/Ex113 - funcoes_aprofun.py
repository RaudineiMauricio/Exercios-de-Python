# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

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


num = leiaInt("Digite um valor: ")
print(f"O valor Digitado foi {num}")
help(leiaInt)