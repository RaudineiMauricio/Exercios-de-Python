#REFAÇA O DESAFIO 35 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO
# - EQUILÁTERO: Todos os lados iguais
# - ISÓCELES: DOIS LADOS IGUAIS, UM DIFERENTE
# - ESCALENO: TODOS OS LADOS DIFERENTES   

r1 = float(input("Digite o Primeiro Seguimento: "))
r2 = float(input("Digite o Segundo Seguimento: "))
r3 = float(input("Digite o Terceiro Seguimento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print("Os segmentos acima PODEM FORMAR UM TRIÂNGULO ", end="")
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 != r2 != r3 !=r1: #AQUI TEVE QUE USAR MAIS UM R1 POR QUE O R3 NÃO FOI COMPARADO AO R1
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print("Os Seguimentos Acima não podem formar um triângulo ")