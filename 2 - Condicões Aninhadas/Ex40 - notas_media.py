#CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE A MÉDIA MOSTGRANDO MA MENSAGEM NO FINAL, 
#DE ACORDO COM A MÉDIA ATINGIDA:
# - MÉDIA ABAIXO DE 5.0: REPROVADO
# - MÉDIA ENTRE 5.0 E 6.9 RECUPERAÇÃO
# - MÉDIA 7.0 OU SUPERIOR : APROVADO

nota1 = float(input("Digite a Primeira Nota: "))
nota2 = float(input("Digite a Segunda Nota: "))

media = (nota1 + nota2)/2
if media < 5:
    print(f"Sua media foi de {media} e voce foi REPROVADO")
elif media <= 5 or media <= 6.9:
    print(f"Sua media foi de {media} e Voce ficou de RECUPERAÇÃO")
elif media >= 7:
    print(f"Parabéns voce Está APROVADO!! sua média foi {media}")

