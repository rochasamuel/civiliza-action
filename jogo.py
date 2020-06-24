from instanciadores import *
from elementos import *
import numpy as np
import random


"""
Necessidades do jogo

"""

def atualizarInteracoesFixas(mundo):
    """
    Re-aplica o efeito das interações fixas do mundo.
    :param mundo: objeto Mundo()
    :return: None
    """

    for interacao in mundo.interacoesFixas:
        if interacao.inicio == mundo.dia:
            interacao.fazerEfeito()
    for interacao in mundo.interacoesFixas:
        if interacao.inicio + interacao.vigencia == mundo.dia:
            interacao.fazerEfeito(desfazer = True)

def probabilidadeDeInteracaoFixa(mundo):
    """
    Implementa as regras de geração aleatória de interaçãoFixa
    :return:
    """
    dado = np.random.rand()
    while dado > 0.9:
        createInteracaoFixa(mundo)
        dado = np.random.rand()

def probabilidaDeAcaoAleatoria(mundo):
    """
    Implementa as regras de geração aleatória de ações entre os países

    :return:
    """
    dado = np.random.rand()
    while dado > 0.5:
        createAcaoAleatoria(mundo)
        dado = np.random.rand()


def trocarAno(mundo):
    """
    Passa o turno, e executa ações
    :return:
    """

    # Chama função de gerações aleatórias
    mundo.ano += 1




def gerarObjetivos(jogador):
    """
    Concebe os objetivos macro do jogador: que números atingir ou evitar, com que países, etc.
    :return:
    """
    alvo = random.choice(list(jogador.mundo.paises.keys()))
    atual = jogador.mundo.panorama.geral.loc[jogador.nome,alvo.nome]
    numObj = 2*atual
    return {'alvo':alvo,
            'valor':numObj}


def passarTurno(mundo):
    """
    Chama deus e o mundo (literalmente)
    :param mundo:
    :return:
    """
    probabilidadeDeInteracaoFixa(mundo)
    probabilidaDeAcaoAleatoria(mundo)
    atualizarInteracoesFixas(mundo)
    trocarAno(mundo)

def prepararMundo(mundo):
    """
    Preenche o mundo
    :param mundo:
    :return:
    """

    for l in 'ABCDEF':
        createPais(l,mundo)

    mundo.panorama = Panorama(mundo)

    for _ in range(10):
        probabilidadeDeInteracaoFixa(mundo)
        probabilidaDeAcaoAleatoria(mundo)

    atualizarInteracoesFixas(mundo)


def menuPrincipal(mundo):
    nome = str(input('Qual o seu nome?\n'))
    # criacao jogador

    jogador = Jogador(nome, 'C1',
                              createSetorEconomico,
                              createSetorMilitar,
                              createSetorPrivado,
                              createLider,
                              mundo)

    print(f'Salve Salve {nome}!')

    prepararMundo(mundo)

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
            # Mostrar panorama
            print(mundo.panorama.geral)

        if opcao == 3:
            # Passar o tempo
            passarTurno(mundo)

        if opcao == 9:
            # Sair
            break