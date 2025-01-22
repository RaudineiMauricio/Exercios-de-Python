#Faça um programa que tenha uma função notas()
#que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# – A situação (opcional)
def notas(*n, sit=False):  # Define a função 'notas', que aceita várias notas (*n) e um parâmetro opcional 'sit' (False por padrão).
    # DOC STRING
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    '''
    dados = dict()  # Cria um dicionário vazio para armazenar os dados analisados.
    dados["Total"] = len(n)  # Armazena no dicionário o total de notas fornecidas.
    dados["Maior"] = max(n)  # Armazena no dicionário a maior nota fornecida.
    dados["Menor"] = min(n)  # Armazena no dicionário a menor nota fornecida.
    dados["Média"] = sum(n) / len(n)  # Calcula a média das notas e armazena no dicionário.

    if sit:  # Verifica se o parâmetro opcional 'sit' é verdadeiro.
        if dados["Média"] >= 7:  # Caso a média seja maior ou igual a 7.
            dados["situação"] = "BOA"  # Define a situação como "BOA".
        elif dados["Média"] >= 5:  # Caso a média seja maior ou igual a 5 e menor que 7.
            dados["Situação"] = "RAZOÁVEL"  # Define a situação como "RAZOÁVEL".
        else:  # Caso a média seja menor que 5.
            dados["Situação"] = "RUIM"  # Define a situação como "RUIM".
    
    return dados  # Retorna o dicionário contendo as informações calculadas.
    
    
# Programa principal
resp = notas(9, 10, 1.5, 8.5, sit=False)  # Chama a função 'notas' com algumas notas e 'sit' definido como False.
print(resp)  # Exibe o dicionário retornado pela função.
help(notas)  # Exibe a docstring da função 'notas' como ajuda.

