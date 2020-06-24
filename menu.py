import jogo

nome = str(input('Qual o seu nome?'))
#criacao jogador

opcao = 0

while opcao != 9: 
    print('''
    [1] - Ações
    [2] - Ver Panorama
    [3] - Passar o Turno
    [9] - Terminar Jogo
    ''')

    opcao = int(input('O que você quer fazer?\n'))

    if opcao == 1:
        opcao_acao = 0

        while opcao_acao != 9:
            print('''
            [1] - Setor Economico
            [2] - Setor Militar
            [3] - Setor Privado
            [9] - Retornar
            ''')
            
            opcao_acao = int(input('Maneiro! Mas em qual setor?'))

            if opcao_acao == 1:
                sub_opcao_acao = 0

                while sub_opcao_acao != 9:
                    print('''
                    [1] - Ação 1
                    [2] - Ação 2
                    [9] - Retornar
                    ''')

                    sub_opcao_acao = int(input('Top! E qual ação?'))

                    if sub_opcao_acao == 1:
                        #fazer ação
                        break
                    
                    if sub_opcao_acao == 2:
                        #fazer ação
                        break
                    
                    if sub_opcao_acao == 9:
                        break
                continue

            if opcao_acao == 2:
                sub_opcao_acao = 0

                while sub_opcao_acao != 9:
                    print('''
                    [1] - Ação 1
                    [2] - Ação 2
                    [9] - Retornar
                    ''')

                    sub_opcao_acao = int(input('Top! E qual ação?'))

                    if sub_opcao_acao == 1:
                        #fazer ação
                        pass

                    if sub_opcao_acao == 2:
                        #fazer ação
                        pass

                    if sub_opcao_acao == 9:
                        break
                break
=======
def menuPrincipal():
>>>>>>> Stashed changes

    nome = str(input('Qual o seu nome?'))
    #criacao jogador

    opcao = 0

    while opcao != 9: 
        print('''
        [1] - Ações
        [2] - Ver Panorama
        [3] - Passar o Turno
        [9] - Terminar Jogo
        ''')

        opcao = int(input('O que você quer fazer?\n'))

        if opcao == 1:
            opcao_acao = 0
            cont_opcoes = 0

            if cont_opcoes >= 1:
                print('saihdjlksahdnkas')
                break
<<<<<<< Updated upstream

    if opcao == 2:
        #Mostrar panorama
        mundo.mostrarPanorama()

    if opcao == 3:
        #Passar o tempo
        jogo.passarTurno(mundo)

    if opcao == 9:
        #Sair
        break
=======
            
            while opcao_acao != 9:
                print('''
                [1] - Setor Economico
                [2] - Setor Militar
                [3] - Setor Privado
                [9] - Retornar
                ''')
                
                opcao_acao = int(input('Maneiro! Mas em qual setor?'))

                if opcao_acao == 1:
                    sub_opcao_acao = 0

                    while sub_opcao_acao != 9:
                        print('''
                        [1] - Ação 1
                        [2] - Ação 2
                        [9] - Retornar
                        ''')

                        sub_opcao_acao = int(input('Top! E qual ação?'))

                        if sub_opcao_acao == 1:
                            cont_opcoes += 1
                            #fazer ação
                            break
                        
                        if sub_opcao_acao == 2:
                            cont_opcoes += 1
                            #fazer ação
                            break
                        
                        if sub_opcao_acao == 9:
                            break
                    break

                if opcao_acao == 2:
                    sub_opcao_acao = 0

                    while sub_opcao_acao != 9:
                        print('''
                        [1] - Ação 1
                        [2] - Ação 2
                        [9] - Retornar
                        ''')

                        sub_opcao_acao = int(input('Top! E qual ação?'))

                        if sub_opcao_acao == 1:
                            cont_opcoes += 1
                            #fazer ação
                            pass

                        if sub_opcao_acao == 2:
                            cont_opcoes += 1
                            #fazer ação
                            pass

                        if sub_opcao_acao == 9:
                            break
                    break

                if opcao_acao == 3:
                    sub_opcao_acao = 0

                    while sub_opcao_acao != 9:
                        print('''
                        [1] - Ação 1
                        [2] - Ação 2
                        [9] - Retornar
                        ''')

                        sub_opcao_acao = int(input('Top! E qual ação?'))

                        if sub_opcao_acao == 1:
                            cont_opcoes += 1
                            #fazer ação
                            pass

                        if sub_opcao_acao == 2:
                            cont_opcoes += 1
                            #fazer ação
                            pass

                        if sub_opcao_acao == 9:
                            break
                    break

                if opcao_acao == 9:
                    break

        if opcao == 2:
            #Mostrar panorama
            pass

        if opcao == 3:
            #Passar o tempo
            pass

        if opcao == 9:
            #Sair
            break

menuPrincipal()
>>>>>>> Stashed changes
