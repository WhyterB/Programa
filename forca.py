import random

def escolher_palavra():
    # Lista de palavras para o jogo de forca
    palavras = ["python", "programacao", "javascript", "algoritmo", "desenvolvimento", "estrutura", "repositorio"]
    return random.choice(palavras)

def mostrar_palavra(palavras, adivinhar_palavra):
    # Exibe a palavra com as letras adivinhadas reveladas e os espaços em branco para as letras não adivinhadas
    mostrar = ""
    for letter in palavras:
        if letter in adivinhar_palavra:
            mostrar += letter + " "
        else:
            mostrar += "_"
    return mostrar

def hangman():
    print("Bem-vindo ao Jogo da Forca!")
    palavras = escolher_palavra()
    adivinhar_palavra = []
    tentativas = 6

    while tentativas > 0:
        print("\nPalavra:", mostrar_palavra(palavras, adivinhar_palavra))
        adivinhar = input("Adivinhe uma letra: ").lower()

        if len(adivinhar) != 1 or not adivinhar.isalpha():
            print("Por favor, insira uma única letra válida.")
            continue
        if adivinhar in adivinhar_palavra:
            print("Você já tentou esta letra. Tente outra.")
            continue

        adivinhar_palavra.append(adivinhar)

        if adivinhar not in palavras:
            tentativas -= 1
            print("Errado! Você tem {} tentativas restantes.".format(tentativas))
            if tentativas == 0:
                print("Você perdeu! A palavra correta era '{}'.".format(palavras))
                break
        else:
            if all(letter in adivinhar_palavra for letter in palavras):
                print("Parabéns! Você venceu! A palavra correta era '{}'.".format(palavras))
                break

    jogue_denovo = input("Deseja jogar novamente? (sim/não): ").lower()
    if jogue_denovo == "sim":
        hangman()
    else:
        print("Obrigado por jogar!")

if __name__ == "__main__":
    hangman()
