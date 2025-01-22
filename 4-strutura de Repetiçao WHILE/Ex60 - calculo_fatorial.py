#LEIA UM NUMERO QUALQUER E MOSTRE O SEU FATORIAL:
#EXEMPLO:
#5! = 5 X 4 X 3 X 2 X 1 = 120

numero = int(input("Digite um Número para calcular seu fatorial: "))
fatorial = 1
contador = numero
print(f"Calculando {numero}! = ", end="")
while contador > 0:
    print(f"{contador}", end="")
    print(" x " if contador > 1 else " = ", end="") #PARA DEIAXR O X EM CADA ESPCAO E O = NO FINAL
    fatorial *= contador #Multiplica pelo valor atual do contador
    contador -=1 #VAI DIMINUINDO UM NUMERO DO CONTADOR
print(f"{fatorial}")
