while True: #executa o que está dentro do while True enquanto tudo for verdadeiro

    hotel = [["*", "*", "3", "G"], ["R", "6", "*", "*"]]  # lista dentro de lista pra criar as posições do hotelzinho

    print('HOTELZINHO DOS ANIMAIS ʕ≧ᴥ≦ʔ\n')
    print('Regras')
    print("• O rato não pode ficar ao lado do gato.")
    print("• O cão não pode ficar ao lado do osso.")
    print("• O gato não pode ficar ao lado do cão.")
    print("• O queijo não pode ficar ao lado do rato")

    opcoes = int(input('1 - Jogar 2 - Sair ')) #apresentação do jogo e menu principal
    if opcoes == 2:
        break
    print('Aqui está o hotelzinho dos animais:\n')

    print('\n FASE 1: Coloque no hotelzinho mais um gato e mais um rato\n')
    for linha in hotel:
        print(linha)

    posGato = int(input("Selecione a posição do Gato "))
    posRato = int(input("Selecione a posição do Rato ")) #atribui a posição dos animais na variavel

    if posGato == 3 and posRato == 6:
        hotel[0][2] = 'G'
        hotel[1][1] = 'R' #de acordo com o valor da variável, muda o valor da respectiva posição na lista
        for linha in hotel:
            print(linha) #imprime as duas listas dentro da lista hotel para o usuário visualizar o jogo
        print('Você venceu!')
        (print('------------'))
        menu = input('Aperte qualquer tecla pra continuar ou 2 pra sair')
        if menu == 2:
            break

    else:
        print('Game Over\n')
        opcoes = int(input('1 - Jogar de novo 2 - Sair '))
        if opcoes == 1:
            continue
        elif opcoes == 2:
            break



    #fase 2
    print('\n FASE 2: Coloque no hotelzinho cão, cão e osso.\n Estão livres os quartos 1, 7 e 8.\n')
    print("• O cão não pode ficar ao lado do osso.\n")
    hotel = [["1", "*", "*", "*"], ["*", "C", "7", "8"]]
    for linha in hotel:
        print(linha)

    posCao1 = int(input('Escolha a ´posição do primeiro cão: '))
    posCao2 = int(input('Escolha a posição do segundo cão: '))
    posOsso = int(input('Escolha a posição do osso: ')) #atribui a posição dos animais na variavel

    if posOsso == 1 and posCao1 == 7 and posCao2 == 8:
        hotel[0][0] = 'O'
        hotel[1][2] = 'C'
        hotel[1][3] = 'C' #de acordo com o valor da variável, muda o valor da respectiva posição na lista
        for linha in hotel:
            print(linha) #imprime as duas listas dentro da lista hotel para o usuário visualizar o jogo
        print('Você venceu!')
        print('------------')
        menu = input('Aperte qualquer tecla pra continuar ou 2 pra sair')
        if menu == 2:
            break
    elif posOsso == 1 and posCao1 == 8 and posCao2 == 7:
        hotel[0][0] = 'O'
        hotel[1][2] = 'C'
        hotel[1][3] = 'C' #de acordo com o valor da variável, muda o valor da respectiva posição na lista
        for linha in hotel:
            print(linha) #imprime as duas listas dentro da lista hotel para o usuário visualizar o jogo
        print('Você venceu!')
        print('------------')
        menu = input('Aperte qualquer tecla pra continuar ou 2 pra sair')
        if menu == 2:
            break
    else:
        print('Game Over\n')
        opcoes = int(input('1 - Jogar de novo 0 - Sair '))
        if opcoes == 1:
            continue
        elif opcoes == 2:
            break

    #fase 3

    print('\n FASE 3: Agora você vai colocar no hotelzinho Gato, Rato e Osso.\n Estão livres os quartos 1, 5, 6 e 7.\n')
    print("• O rato não pode ficar ao lado do gato.")
    hotel = [["1", "*", "*", "*"], ["5", "G", "7", "*"]]
    for linha in hotel:
        print(linha) #imprime as duas listas dentro da lista hotel para o usuário visualizar o jogo

    poGato = int(input('Escolha a posição do gato: '))
    poRato = int(input('Escolha a posição do rato: '))
    poOsso = int(input('Escolha a posição do osso: ')) #atribui a posição dos animais na variavel

    if poRato == 1 and poOsso == 5 and poGato == 7:
        hotel[0][0] = 'R'
        hotel[1][0] = 'O'
        hotel[1][2] = 'G' #de acordo com o valor da variável, muda o valor da respectiva posição na lista
        for linha in hotel:
            print(linha) #imprime as duas listas dentro da lista hotel para o usuário visualizar o jogo
        print('Você venceu!')
        print('------------')
        menu = input('Aperte qualquer tecla pra continuar ou 2 pra sair')
        if menu == 2:
            break

    else:
        print('Game Over\n')
        opcoes = int(input('1 - Jogar de novo 0 - Sair '))
        if opcoes == 1:
            continue
        elif opcoes == 2:
            break

    #fase 4


    print('\n FASE 4: Queijo, queijo e osso. Nessa última fase você deve por esses 3.\n Estão livres os quartos 1, 5, 6 e 7.\n')
    print("• O queijo não pode ficar perto do rato e o osso não pode ficar perto do cachorro.")
    hotel = [["1", "2", "3", "*"], ["*", "R", "*", "*"]]
    for linha in hotel:
        print(linha)  #imprime as duas listas dentro da lista hotel para o usuário visualizar o jogo

    poQueijo1 = int(input('Escolha a posição do primeiro queijo: '))
    poQueijo2 = int(input('Escolha a posição do segundo queijo: '))
    poOsso = int(input('Escolha a posição do osso: ')) #atribui a posição dos animais na variavel

    if poOsso == 2:
        hotel[0][1] = 'O'
        hotel[0][0] = 'Q'
        hotel[0][2] = 'Q' #de acordo com o valor da variável, muda o valor da respectiva posição na lista
        for linha in hotel:
            print(linha) #imprime as duas listas dentro da lista hotel para o usuário visualizar o jogo
        print('Você venceu!')
        print('------------')
        print('╚═ ͡° ͜ʖ ͡°)═╝')
        print('╚═(███)═╝')
        print('╚═(███)═╝')
        print('.╚═(███)═╝')
        print('..╚═(███)═╝')
        print('…╚═(███)═╝')
        print('…╚═(███)═╝')
        print('..╚═(███)═╝')
        print('.╚═(███)═╝')
        print('╚═(███)═╝')
        print('.╚═(███)═╝')
        print('..╚═(███)═╝')
        print('…╚═(███)═╝')
        print('…╚═(███)═╝')
        print('…..╚(███)╝')
        print('……╚(██)╝')
        print('………(█)')
        print('Obrigado por jogar o Hotelzinho dos Animais')
        menu = input('Aperte 2 pra voltar ao menu principal')
        if menu == 2:

            break #usuário venceu o jogo e o jogo foi finalizado

    else:
        print('Game Over\n')
        opcoes = int(input('1 - Jogar de novo 0 - Sair '))
        if opcoes == 1:
            continue
        elif opcoes == 2:
            break #caso o usuário falhe em alguma das fases o jogo é reiniciado do zero



