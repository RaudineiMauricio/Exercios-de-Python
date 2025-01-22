'''def soma(a, b):
    s = a + b
    print(s)
#PROGRRAM PRINCIPAL
soma(4, 5)
soma(8, 9)
soma(2, 1)'''

def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma de A + B = {s}")
#PROGRAMA PRINCIPAL
soma(b=4, a=5)
soma(7, 2)

#função para receber vários valores e somar (desempacotamento)
def contador(* num):
    tamanho = len(num)
    print(f"Recebi os valores {num} e são ao todo{tamanho} números")

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


#função para dobrar os valores de uma lista
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
