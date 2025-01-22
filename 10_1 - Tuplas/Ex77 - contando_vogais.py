#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ("mamao", "manga", "abacaxi", "melao", "uva", "onibus",
            "carro", "aviao", "sandalia", "tenis", "flamengo", "botafogo",
            "bolo", "faca", "marmita", "metro", "brasil")

for p in palavras:
    print(f"\nNa palavra {p.upper()} Temos ", end="") #DESTA AS PALAVRAS PRA MAIÚSCULAS
    for letra in p: #PERCORRE TODAS AS LETRAS POR QUE CADA PALAVRA É UMA LISTA, E VERIFICA SE TEM AS VOGAIS
        if letra.lower() in "aeiou": # SE TIVER JOGA TUDO PRA LETRAS MINÚSCULAS E MOSTRA AS VOGAIS
                print(letra, end=" ")
