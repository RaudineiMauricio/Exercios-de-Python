#FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA,
#MAS SÓ ACEITE  OS VALORES "M" OU "F".
#CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO


sexo = str(input("Informe o seu sexo: [M/F] ")).strip().upper()[0] #Esse [0] é para pegar a primeira letra digitada.
while sexo not in "mMFf": #ENQUANTO O SEXO DIGITADO NAO FOR essa opção, nao deixa avançar
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso.")