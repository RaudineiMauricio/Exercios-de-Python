# Crie um programa que tenha uma função fatorial()
# que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    '''
    -> CALCULA O FATORIAL DE UM NÚMERO
    :PARAM N: O NÚMERO A SER CALCULADO
    :PARAM SHOW: (OPCIONAL) MOSTRA OU NÃO A CONTA
    :RETURN: O VALOR DO FARORIAL DE UM NÚMERO N.
    '''
    
    f = 1
    for c in range(n, 0, -1):
        if fatorial:
            if show:
                print(c, end="")
                if c > 1:
                    print( " x ", end="")
                else:
                    print(" = ", end="")
        f *= c
    return f



#PROGRAMA PRINCIPAL
print(fatorial(5, show=True))
help (fatorial)