import random

opcoes = ["pedra", "papel", "tesoura"]

pontos_jogador = 0
pontos_computador = 0


melhor_de_3 = 1

while melhor_de_3 < 4:

    jogador = input("Escolha pedra, papel ou tesoura: ")
    if jogador not in opcoes:
        print("Escolha inválida")
        continue

    computador = random.choice(opcoes)

    print("Computador escolheu:", computador)



    if jogador == computador:
        print('empate')

    elif jogador == 'pedra' and computador == 'tesoura':
        print('Voce ganhou!')
        pontos_jogador += 1


    elif jogador == 'tesoura' and computador == 'papel':
        print('Voce ganhou!')
        pontos_jogador += 1


    elif jogador == 'papel' and computador == 'pedra':
        print('Voce ganhou!')
        pontos_jogador += 1

    else:
        print('Voce perdeu!!')
        pontos_computador += 1



    melhor_de_3 += 1
    print(pontos_computador)
    print(pontos_jogador)


    jogar_novamente = input("Quer jogar novamente? ")

    if jogar_novamente != "sim":
        break
