from instanciadores import *
from classes import *
import numpy as np


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
        if interacao.vigencia



    def probabilidadeDeInteracaoFixa(mundo):
        """
        Implementa as regras de geração aleatória de interaçãoFixa
        :return:
        """
        pass


def trocarAno(mundo):
    """
    Passa o turno, e executa ações
    :return:
    """

    # Chama função de gerações aleatórias
    mundo.ano += 1


    def probavilidaDeAcaoAleatoria():
        """
        Implementa as regras de geração aleatória de ações entre os países

        :return:
        """
        pass

def gerarObjetivos():
    """
    Concebe os objetivos macro do jogador: que números atingir ou evitar, com que países, etc.
    :return:
    """
    pass

def testarObjetivo():
    """
    Verifica se o objetivo ou as restrições foram atingidas.
    :return:
    """

    pass