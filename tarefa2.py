import random

print("Escolha o nível de dificuldade:")
print("1 - Fácil (1 a 10)")
print("2 - Médio (1 a 20)")
print("3 - Difícil (1 a 30)")

opcao = input("Digite o número da opção: ")

if opcao == "1":
    minimo = 1
    maximo = 10
elif opcao == "2":
    minimo = 1
    maximo = 20
elif opcao == "3":
    minimo = 1
    maximo = 30
else:
    print("Opção inválida! Vou usar o modo Fácil (1 a 10).")
    minimo = 1
    maximo = 30

jogar_de_novo = "s"

while jogar_de_novo == "s":
    numero_sorteado = random.randint(minimo, maximo)
    tentativa = 1
    acertou = False

    print("")
    print("Adivinhe o número entre", minimo, "e", maximo)

    while tentativa <= 3 and acertou == False:
        chute = int(input("Tentativa " + str(tentativa) + " de 3 - Digite um número: "))

        if chute == numero_sorteado:
            print("Parabéns, você acertou!")
            acertou = True
        else:
            print("Você errou!")
            if chute < numero_sorteado:
                print("Tente um número maior")
            else:
                print("Tente um número menor")

        tentativa = tentativa + 1

    if acertou == False:
        print("Você perdeu! Fim de jogo.")
        print("O número sorteado era", numero_sorteado)

    jogar_de_novo = input("Deseja jogar novamente? (s/n): ")

print("Obrigado por jogar!")

