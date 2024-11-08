#FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM A SUA IDADE, SE ELE AINDA VAI SE ALISTAR
#AO SERVIÇO MILITAR, SE E Á HORA EXATA DE SE ALISTAR OU SE JÁ PASSOU DO TEMPO DE ALISTAMENTO.
#SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU PASSOU DO PRAZO.

#BIBLIOTECAS PRA DATAS
from datetime import date

atual = date.today().year # ANO ATUAL
nascimento = int(input("Ano de Nascimento: "))
idade = atual - nascimento
print(f"Quem nasceu em {nascimento} tem {idade} anos em {atual}")

#LÓGICA PARA VERIFICAR A IDADE
if idade ==18:
    print("Voce tem que se alistar IMEDIATAMENTE!!")
elif idade < 18:
    saldo = 18 - idade
    print(f"Ainda faltam {saldo} anos para o seu Alistamento")
    ano = atual + saldo   #PARA SABER EM QUE ANO VAI SER O ALISTAMENTO E QUANTO TEMPO FALTA
    print(f"Seu alistamento será em {saldo} anos")
elif idade > 18:
    saldo = idade - 18 
    print(f"Voce já deveria ter se alistado há {saldo} anos")
    ano = atual - saldo #PARA SABER EM QUE ANO DEVERIA TER SE ALISTADO
    print(f"Seu alistamento foi em {ano}")