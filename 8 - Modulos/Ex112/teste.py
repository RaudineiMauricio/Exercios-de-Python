#Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
#Transfira todas as funções utilizadas nos desafios 107, 108 e 109
#para o primeiro pacote e mantenha tudo funcionando.
from utilidadescev import moeda
from utilidadescev import dado


preco = dado.leiaDinheiro("Digite o preco: R$")
moeda.resumo(preco, 20, 12)