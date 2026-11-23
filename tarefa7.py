
palavra = "PYTHON"

letras_descobertas = []
letras_utilizadas = []

erros = 0
limite_erros = 6

print("=" * 35)
print("         JOGO DE ADIVINHACAO")
print("=" * 35)

while erros < limite_erros:

    print("\nPalavra: ", end="")

    for letra in palavra:
        if letra in letras_descobertas:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"\nErros: {erros}/{limite_erros}")

    descobriu_tudo = True
    for letra in palavra:
        if letra not in letras_descobertas:
            descobriu_tudo = False

    if descobriu_tudo:
        break

    palpite = input("Digite uma letra: ").upper()

    if len(palpite) != 1 or not palpite.isalpha():
        print("Entrada invalida! Digite apenas UMA letra.")
        continue

    if palpite in letras_utilizadas:
        print("Voce ja tentou essa letra!")
        continue

    letras_utilizadas.append(palpite)

    if palpite in palavra:
        letras_descobertas.append(palpite)
        print("Voce acertou!")
    else:
        erros += 1
        print("Palpite incorreto!")

print("\n" + "=" * 35)

if erros < limite_erros:
    print("PARABENS! Voce venceu!")
else:
    print("Que pena! Voce perdeu!")

print(f"A palavra secreta era: {palavra}")

print("=" * 35)
