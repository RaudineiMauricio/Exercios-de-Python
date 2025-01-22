def leiaDinheiro(msg):
    # Define a função leiaDinheiro que recebe uma mensagem (msg) como argumento.

    valido = False
    # Cria uma variável chamada 'valido' para controlar o loop. Inicialmente, é definida como False.

    while not valido:
        # Enquanto 'valido' for False, o loop continuará executando.

        entrada = str(input(msg)).replace(",", ".").strip()
        # Solicita ao usuário uma entrada usando a mensagem (msg) fornecida.
        # Substitui vírgulas (",") por pontos (".") para compatibilidade com números decimais.
        # Remove espaços em branco no início e no final da string usando 'strip'.

        if entrada.isalpha() or entrada == "":
            # Verifica se a entrada é composta apenas por letras (isalpha) ou está vazia.

            print(f"\033[0;31mERRO: \"{entrada}\" é um pacote inválido!\033[m")
            # Exibe uma mensagem de erro em vermelho, indicando que a entrada é inválida.

        else:
            valido = True
            # Se a entrada for válida (não letras ou vazia), define 'valido' como True para encerrar o loop.

            return float(entrada)
            # Converte a entrada para um número de ponto flutuante (float) e a retorna.

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("ERRO! Digite um número inteiro válido.")
        if ok:
            break
    return valor