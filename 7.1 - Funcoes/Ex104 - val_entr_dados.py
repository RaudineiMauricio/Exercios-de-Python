#Crie um programa que tenha a função leiaInt()
#que vai funcionar de forma semelhante ‘a função input() do Python,
#só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt(n):
    while True:
        num = input(n)
        if num.isnumeric():
            num = int(num)
            break
        else:
            print("ERRO! Digite um número inteiro válido.")
    return num



#PROGRAMA PRINCIPAL
n = leiaInt("Digite um numero: ")
print(f"Você digitou o número {n} ")

#SOLUÇÃO DO PROFESSOR
'''
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("ERRO! Digite um número inteiro válido.")
        if ok:
            break
    return valor


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")'''