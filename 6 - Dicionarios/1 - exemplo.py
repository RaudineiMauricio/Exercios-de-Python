pessoas = {"nome": "Gustavo", "sexo": "M", "idade": 22}


#alterando valor dentro do dicionario
pessoas["nome"] = "Leandro"

#adicionando elementos
pessoas["peso"] = 98.5

print(f"O {pessoas["nome"]} tem {pessoas["idade"]} anos ")

#outra forma de mostrar os dados
''''pessoas = {"nome": "Gustavo", "sexo": "M", "idade": 22}
print(pessoas.keys()) #mostra a chave dos dados, por exemplo nome, sexo, idade.

pessoas = {"nome": "Gustavo", "sexo": "M", "idade": 22}
print(pessoas.values()) #mostra a chave dos dados, por exemplo nome, sexo, idade. #mostra os valores que as chaves fazem referência

pessoas = {"nome": "Gustavo", "sexo": "M", "idade": 22}
print(pessoas.items()) #mostra a chave dos dados, por exemplo nome, sexo, idade. #mostra os valores que as chaves fazem referência

for k in pessoas.keys(): #mostra a chave dos dados
    print(k)
'''
for k, v in pessoas.items(): #mostra a chave e o valor de cada dado no dicionário 
    print(f"{k} = {v}")


#Para deletar um elemento
#del pessoas["nome"]

#criando dicionário dentro de uma lista

''''brasil = []
estado1 = {"uf": "Rio de Janeiro", "Sigla": "RJ"}
estado2 = {"uf": "São Paulo", "Sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]["Sigla"])'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Silga do Estado: "))
    brasil.append(estado.copy()) #cRIA UMA COPIA DE ESTADO, PODE QUE NO DICIONÁRIO NAO DA PARA FAZER FATIAMEMTO [:]
for e in brasil: #para cada valor em brasil
    for v in e.values(): #para cada valor nos valores de estado
        print(v, end=" ") 
    print()
