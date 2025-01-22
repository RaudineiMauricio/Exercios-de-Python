#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
#Faça também um programa que importe esse módulo e use algumas dessas funções.


def aumentar(preco, taxa):
    resp = preco + (preco * taxa/100)
    return resp


def diminuir(preco, taxa):
    resp = preco - (preco * taxa/100)
    return resp


def dobro(preco):
    resp = preco * 2
    return resp


def metade(preco):
    resp = preco / 2
    return resp