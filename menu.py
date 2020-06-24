import jogo
import classes
import instanciadores as inst
import numpy as np

def menuPrincipal(mundo):

    nome = str(input('Qual o seu nome?\n'))
    #criacao jogador

    jogador = classes.Jogador(nome, 'C1',
                              inst.createSetorEconomico,
                              inst.createSetorMilitar,
                              inst.createSetorPrivado,
                              inst.createLider,
                              mundo)

    print(f'Salve Salve {nome}!')

    jogo.prepararMundo(mundo)

    opcao = 0
    cont_opcoes = 0

    while opcao != 9: 
        print('''
        [1] - Ações
        [2] - Ver Panorama
        [3] - Passar o Turno
        [9] - Terminar Jogo
        ''')

        opcao = int(input('O que você quer fazer?\n'))

        if opcao == 1:
            if cont_opcoes == 1:
                print('Tá querendo hackear??')
                continue

            lista_de_paises = [p.lower() for p in mundo.paises.keys()]

            # Pedir pra escolher alvo
            alvo = 'Nenhuma'
            while alvo not in lista_de_paises:
                alvo = (input(f'Dos seguintes paises:\n{lista_de_paises}\nDigite exatamente o seu alvo.\n')).lower()

            fator = np.random.rand()

            opcao_acao = 0
            
            while opcao_acao != 9:
                print('''
                [1] - Setor Economico
                [2] - Setor Militar
                [3] - Setor Privado
                [9] - Retornar
                ''')
                
                opcao_acao = int(input('Maneiro! Mas em qual setor?\n'))

                if opcao_acao == 1:
                    sub_opcao_acao = 0

                    while sub_opcao_acao != 9:
                        print('''
                        [1] - Ação 1
                        [2] - Ação 2
                        [9] - Retornar
                        ''')

                        sub_opcao_acao = int(input('Top! E qual ação?\n'))

                        if sub_opcao_acao == 1:
                            cont_opcoes = 1
                            jogador.acoesDeJogador[opcao_acao][sub_opcao_acao].fazerEfeito(alvo, fator)
                            break
                        
                        if sub_opcao_acao == 2:
                            cont_opcoes = 1
                            jogador.acoesDeJogador[opcao_acao][sub_opcao_acao].fazerEfeito(alvo, fator)
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
                            cont_opcoes = 1
                            jogador.acoesDeJogador[opcao_acao][sub_opcao_acao].fazerEfeito(alvo, fator)
                            pass

                        if sub_opcao_acao == 2:
                            cont_opcoes = 1
                            jogador.acoesDeJogador[opcao_acao][sub_opcao_acao].fazerEfeito(alvo, fator)
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
                            cont_opcoes = 1
                            jogador.acoesDeJogador[opcao_acao][sub_opcao_acao].fazerEfeito(alvo, fator)
                            pass

                        if sub_opcao_acao == 2:
                            cont_opcoes = 1
                            jogador.acoesDeJogador[opcao_acao][sub_opcao_acao].fazerEfeito(alvo, fator)
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

