#CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA
#COM UMA CONTAGEM POR EXTENSO, DE ZERO ATÉ VINTE.
#SEU PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO(ENTRE 0 E 20)
#E MOSTRÁ-LO POR EXTENSO

valores = ("ZERO", "UM", "DOIS", "TRÊS", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE", "DEZ",
           "ONZE", "DOZE", "TREZE", "CATORZE", "QUINZE", "DEZESEIS", "DEZESETE", "DEZOITO",
           'DEZENOVE', "VINTE")

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num <= 20:
        print(f"Você digitou o número {valores[num]}") #pega o valor e referencia do indice num
    else:
        print("Tente novamente. ", end="")
    
    res = " "
    while res not in "SN":
        res = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if res == "N":
        break
print("PROGRAMA ENCERRADO.")

               