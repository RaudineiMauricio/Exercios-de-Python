#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
#Faça também um programa que importe esse módulo e use algumas dessas funções.


def aumentar(preco = 0, taxa = 0, formato=False):
    resp = preco + (preco * taxa/100)
    return resp if formato is False else moeda(resp)


def diminuir(preco = 0, taxa = 0, formato=False):
    resp = preco - (preco * taxa/100)
    return resp if formato is False else moeda(resp)



def dobro(preco = 0, formato=False):
    resp = preco * 2
    return resp if formato is False else moeda(resp)


def metade(preco = 0, formato=False):
    resp = preco / 2
    return resp if formato is False else moeda(resp)



def moeda(preco = 0, moeda = "R$"):
    return f"{moeda}{preco:>.2f}".replace(".", ",")

def resumo(preco = 0, taxaa = 10, taxar=5):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preco analisado: \t{moeda(preco)}")
    print(f"Dobro do preco: \t{dobro(preco, True)}")
    print(f"Metade do preco: \t{metade(preco, True)}")
    print(f"{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}")
    print(f"{taxar}% de redução: \t\t{diminuir(preco, taxar, True)}")
    print("-" * 30)

