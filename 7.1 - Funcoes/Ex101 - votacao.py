#Crie um programa que tenha uma função chamada voto()
#que vai receber como parâmetro o ano de nascimento de uma pessoa,
#retornando um valor literal indicando se uma pessoa tem voto NEGADO,
#OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date  # Importa a função 'date' do módulo 'datetime' para trabalhar com datas

# Função para verificar a obrigatoriedade do voto com base no ano de nascimento
def voto(ano):
    from datetime import date  # Importa novamente a função 'date' para uso dentro da função
    atual = date.today().year  # Obtém o ano atual
    idade = atual - ano  # Calcula a idade com base no ano de nascimento
    # Verifica se a idade é menor que 16
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA."
    # Verifica se a idade está entre 16 e 18 (inclusive) ou maior que 65
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        # Para idades entre 18 e 65, o voto é obrigatório
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"
     
# Solicita ao usuário o ano de nascimento
nasc = int(input("Em que ano você nasceu? "))
# Chama a função 'voto' passando o ano de nascimento e exibe o resultado
print(voto(nasc))
