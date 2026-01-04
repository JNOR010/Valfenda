def jogo_adivinhacao_palavra():
 
    palavra_secreta = "LIAM"  
    letras_corretas = []       
    tentativas = 0             

    print("Bem-vindo ao jogo de adivinhação de palavras!")
    print("A palavra tem {} letras.".format(len(palavra_secreta)))

    
    while True:
        # 1. Mostrar o estado atual da palavra (com * para letras não adivinhadas)
        palavra_mostrada = ""
        for letra in palavra_secreta:
            if letra in letras_corretas:
                palavra_mostrada += letra + " "
            else:
                palavra_mostrada += "* "
        print("\nPalavra atual:", palavra_mostrada)

        # Verificar se o jogo acabou
        if "*" not in palavra_mostrada:
            print("\nParabéns! Você adivinhou a palavra corretamente: {}!".format(palavra_secreta))
            break

        # 2. Pedir uma letra ao usuário
        tentativa_letra = input("Digite uma letra (ou 'sair' para desistir): ").strip().upper()

        if tentativa_letra == 'SAIR':
            print("Jogo encerrado. A palavra era: {}".format(palavra_secreta))
            break

        # Validar a entrada (deve ser apenas uma única letra)
        if len(tentativa_letra) != 1 or not tentativa_letra.isalpha():
            print("Entrada inválida. Digite apenas uma única letra.")
            continue

        # 3. Verificar a letra
        if tentativa_letra in letras_corretas:
            print("Você já tentou a letra '{}'. Tente outra.".format(tentativa_letra))
        elif tentativa_letra in palavra_secreta:
            print("Parabéns! A letra '{}' está na palavra.".format(tentativa_letra))
            letras_corretas.append(tentativa_letra)
        else:
            print("Que pena. A letra '{}' não está na palavra.".format(tentativa_letra))

        tentativas += 1

    print("Você fez um total de {} tentativas.".format(tentativas))
# Para rodar o jogo, chame a função:
if __name__ == "__main__":
    jogo_adivinhacao_palavra()