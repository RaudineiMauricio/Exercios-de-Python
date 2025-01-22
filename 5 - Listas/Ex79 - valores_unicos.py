#  Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#  Caso o número já exista lá dentro, ele não será adicionado.
#  No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = []
continuar = True
print("Bem vindo ao programa do RaulJoga10!")
while continuar:
    num = (int(input("Digite um valor: ")))
    if num not in valores:
        valores.append(num)
        print("Valor adicionado com Sucessso!")
    else:
        print("Valor duplicado! Não irei adicionar!")

    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
        if resp not in "SN":
            print("Opção inválida, tente novamente.")
    continuar = resp == "S"

print("-=" * 30)
valores.sort()  # Ordena os valores
print(f"Sua lista final: {valores}")

