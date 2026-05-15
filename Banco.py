saldo = 1000
extrato = []

tentativas = 0
senha = '1234'
while tentativas < 3:
    tentativas += 1
    chute = input('Digite a senha: ')


    if chute != senha:
        print('TENTE NOVAMENTE!!')

    if chute != senha and tentativas == 3:
        print('\n------------')
        print("Conta bloqueada!")

    while chute == senha:



        print('\n------Banco----')
        print('1 - Ver saldo')
        print('2 - Depositar')
        print('3 - Sacar')
        print('0 - Sair')

        opcao = int(input('Escolha uma opcao: '))

        if opcao == 1:
            print('Seu saldo e:',saldo)


        elif opcao == 2:
            depositar = int(input('Qual a quantidade de deposito: '))
            if depositar > 0:
                saldo += depositar
                print('DEPOSITO REALIZADO!')
                extrato.append(f'+{depositar}')

            else:
                print('NUMERO INVALIDO!')



        elif opcao == 3:
            saque = int(input('Quantos voce quer retirar: '))
            if saque <= saldo:
                saldo -= saque
                print('SAQUE REALIZADO!!')
                extrato.append(f'-{saque}')

            else:
                print('SALDO INSUFICIENTE')

        elif opcao == 0:
            print('\n -----Sistema desligado---')
            break

        print('Extrato:', extrato)