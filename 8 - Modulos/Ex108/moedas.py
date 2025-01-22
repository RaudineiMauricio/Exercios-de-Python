#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
#Faça também um programa que importe esse módulo e use algumas dessas funções.


def aumentar(preco = 0, taxa = 0):
    resp = preco + (preco * taxa/100)
    return resp


def diminuir(preco = 0, taxa = 0):
    resp = preco - (preco * taxa/100)
    return resp


def dobro(preco = 0):
    resp = preco * 2
    return resp


def metade(preco = 0):
    resp = preco / 2
    return resp


def moeda(preco = 0, moeda = "R$"):
    return f"{moeda}{preco:>.2f}".replace(".", ",")