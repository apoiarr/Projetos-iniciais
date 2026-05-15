import random
tentativas = 0
numero_secreto = random.randint(1,100)

while tentativas < 5:
    tentativas += 1
    jogador = int(input('Escolhe um numero: '))

    if numero_secreto > jogador:
        print('O numero e maior!')
        print(f'Tentativas: {tentativas}')

    elif numero_secreto < jogador:
        print('O numero e menor!')
        print(f'Tentativas: {tentativas}')

    elif jogador == numero_secreto:
        print('Voce acertou!!')
        print(f'Tentativas: {tentativas}')
        break

print("Você perdeu!")
print("O número era:", numero_secreto)