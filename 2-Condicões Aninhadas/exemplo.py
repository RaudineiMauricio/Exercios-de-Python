nome = str(input(" Qual é seu nome? "))

#PODE USAR VÁRIOS ELIF, MAS NAO PODE USAR ELIF SEM COMEÇAR COM IF.
if nome == "Gustavo":
    print("Que nome Bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome é bem popular no Brasil!!")
elif nome in "Ana Claúdia Jéssica Juliana":
    print("Belo nome Feminino!!")
#O USO DO ELSE É OPICIONAL 
else:
    print("Seu nome é normal.")
print(f"Tenha um Bom Dia, {nome}")
