#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUÁRIO SE ELAS PODEM OU NAO FORMAR UM TRIÂNGULO

#ILUSTRANDO A INTERFACE DO CÓDIGO
print("-=-"*20)
print("Analisador de Triângulo")
print("-=-"*20)

r1 = float(input("Primeiro seguimento: "))
r2 = float(input("Segundo Seguimento: "))
r3 = float(input("Terceiro Seguimento: "))

#LOGICA PARA CALCULAR AS RETAS DO TRIÂNGULO 
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os Numeros acima podem formar Triângulo")
else:
    print("Os Numeros acima nao podem formar Triângulo")