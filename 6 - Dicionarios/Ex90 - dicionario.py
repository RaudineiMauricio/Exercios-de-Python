# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno["nome"] = str(input("Nome: "))
aluno["media"] = float(input(f"Média de {aluno["nome"]} é: "))
if aluno["media"] >= 7:
    aluno["situacao"] = "APROVADO"
elif 5 <= aluno["media"] < 7:
    aluno["situacao"] = "RECUPERACAO"
else:
    aluno["situacao"] = "REPROVADO"
print("-=" * 30)
for k, v in aluno.items():
    print(f" - {k} é igual a {v}")
