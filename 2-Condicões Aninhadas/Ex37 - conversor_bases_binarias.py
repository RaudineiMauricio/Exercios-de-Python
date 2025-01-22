#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO
#1 - BINÁRIO
#2 - OCTAL
#3 - HEXADECIMAL

#PEGADO O NÚMERO INTEIRO PARA CONVERTER, AS ''' SÃO PARA COLOCAR MAIS OPÇOES DENTRO DO PRINT
numero = int(input("Qual número voce deseja converter? "))
print('''Escolha uma das bases de conversão:
      [ 1 ] converter pra BINÁRIO
      [ 2 ] converter para OCTAL
      [ 3 ] converter para HEXADECIMAL''')

opcao = int(input("Sua opção: "))

#BLOCO DE CONDIÇÕES PARA A OPÇAO DESEJADA
if opcao == 1:
    print(f"O número {numero} convertido em BINÁRIO É {bin(numero)[2:]}") #O PYTHON JA TEM O AS CONVERSÕES PRONTAS :)
elif opcao == 2:
    print(f"O número {numero} convertido em OCTAL É {oct(numero)[2:]}") #ESSE [2:] É PARA APARECER APENAS A CONVERSÃO E NAO O 0b11101010  
elif opcao == 3:
    print(f"O número {numero} convertido em HEXADECIMAL É {hex(numero)[2:]}") #O RESULTADO VAI VIR COM 0B PARA DIZER QUE É BINÁRIO E VICE VERSA
else:
    print("Opção Inválida, Tente novamente!")