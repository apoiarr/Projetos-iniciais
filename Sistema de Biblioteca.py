biblioteca = []

while True:
    print('1 - Cadastrar livro')
    print('2 - Listar livros')
    print('3 - Buscar livro pelo título')
    print('4 - Remover livro')
    print('5 - Mostrar livro mais antigo')
    print('6 - Mostrar quantidade de livros')
    print('0 - Sair')

    opcao = int(input('O que deseja fazer: '))

    if opcao == 1:
        titulo = input('Titulo: ')
        autor = input('Autor: ')
        ano = input('Ano: ')

        guardar = {
            'Titulo:':titulo,
            'Autor:':autor,
            'Ano:':ano

        }
        biblioteca.append(guardar)
        print('Livro Adicionado!!!')


    elif opcao == 2:
        if len(biblioteca) <= 0:
            print('Lista vazia!!')
        else:
            for i, guardar in enumerate(biblioteca, start=1):
                print(f'{i}. Titulo:{guardar["Titulo:"]} | Autor:{guardar["Autor:"]} | Ano:{guardar["Ano:"]}')


    elif opcao == 3:
        if len(biblioteca) <= 0:
            print('Lista vazia!!')
        else:
            procurar = input('Procurar Livro: ')
            encontrado = False

            for livro in biblioteca:
                if livro['Titulo:'].lower() == procurar.lower():
                    print(f'Título: {livro["Titulo:"]}')
                    print(f'Autor: {livro["Autor:"]}')
                    print(f'Ano: {livro["Ano:"]}')
                    encontrado = True


                if not encontrado:
                    print('Livro não encontrado!!')

    elif opcao == 4:
        if len(biblioteca) <= 0:
            print('Lista esta vazia!!')
        else:
            remover = input('Remover livro: ')
            encontrado = False

            for livro in biblioteca:
                if livro['Titulo:'].lower() == remover.lower():
                    biblioteca.remove(livro)
                    print('Livro removido!!!')
                    encontrado = True

            if not encontrado:
                print('Livro nao encontrado')

    elif opcao == 5:
        if len(biblioteca) <= 0:
            print('Lista vazia!!')
        else:
            mais_antigo = biblioteca[0]

            for livro in biblioteca:
                if int(livro['Ano:']) < int(mais_antigo['Ano:']):
                    mais_antigo = livro

            print('Livro mais antigo:')
            print(f'Título: {mais_antigo["Titulo:"]}')
            print(f'Autor: {mais_antigo["Autor:"]}')
            print(f'Ano: {mais_antigo["Ano:"]}')




    elif opcao == 6:
        if len(biblioteca) <= 0:
            print('Lista vazia!!')
        else:
            print(f'A quantidade de livros e:{len(biblioteca)}')

    elif opcao == 0:
        print('Sistema desligado!!!')
        break


