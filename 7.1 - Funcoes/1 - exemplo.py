#VARIÁVEL LOCAL E VARIÁVEL GLOBAL
''''
def funcao():
    n1 = 4
    print(f"N1 dentro vale {n1}")

n1 = 2
funcao()
print(f"N1 fora vale {n1}")

'''
''''def teste(b):
    #para usar variável global, localmente, use a palavra GLOBAL e o nome da variável que deseja
    #variável local, só pode ser chamada localmente.
    global a
    a = 8
    b += 4
    c = 2
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")

#variável global, pode ser chamada em qualuer lugar
a = 5
teste(a)
print(f"A fora vale {a}")
    
#USANDO RETURN

def somar(a=0, b=0, c=0):
    s = a + b + c
    #encerra a execução de uma função e retorna um valor para o chamador. 
    #Como funciona?
    #Quando uma função é chamada e encontra o comando return, ela retorna imediatamente ao local de chamada. 
    #O return especifica o valor ou valores a serem passados de volta da função. 
    #Sem o return, a função retornará None por padrão. 
    return s


r1 = somar(3, 2 , 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f"Os resultados foram {r1}, {r2}, {r3}")'''

#exemplo usando fatorial

def fatorial(num=1): #se nao for passado valor pra num ele irá valer 1 
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input("Digite um número: "))
print(f"O fatorial de {n} é igual a {fatorial(n)}")

#OUTRO EXEMPLO DE EXIBIR

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f"Os resultados são {f1}, {f2}, {f3}")

#PARA COMPARAR SE O NUMERO É PAR OU IMPAR USANDO RETURN

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    


num = int(input("Digite um número: "))
if par(num):
    print("É PAR")
else:
    print("NÃO É PAR")