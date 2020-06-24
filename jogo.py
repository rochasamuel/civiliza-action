from instanciadores import *
from classes import *
import numpy as np
import random


"""
Necessidades do jogo

"""


def mostrarMenu():
    """
    Apresentar menu com opções
    1 - Mostrar panorama
    2 - Mostrar menu de categorias de ações
    2.1 - Mostrar menu de ações dentro das categorias
    3 - Passar turno

    :return:
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