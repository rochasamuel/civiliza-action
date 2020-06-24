import pandas as pd
import numpy as np
import random
import string
import elementos as e

def random_string_generator(str_size):
    """
        Função que gera uma string aleatória
        :param str_size: tamanho da string
        :return: retorna a string gerada
    """
    return ''.join(random.choice(string.ascii_letters) for x in range(str_size))

def createSetorEconomico():
    """
        Funcão que instancia um setor economico
        :return: uma instância de um SetorEconomico
    """
    return e.SetorEconomico(
        10,
        12)

def createSetorMilitar():
    """
        Funcão que instancia um setor Militar
        :return: uma instância de um SetorMilitar
    """
    arsenal = {}
    tropa = {}
    
    return e.SetorMilitar(arsenal, tropa)

def createSetorPrivado():
    """
        Funcão que instancia um setor Privado
        :return: uma instância de um SetorPrivado
    """    
    
    importacao = {}
    exportacao = {}
    
    return e.SetorPrivado(importacao, exportacao)

def createLider():
    """
        Funcão que instancia um Lider
        :return: uma instância de um Lider
    """
    nome = random_string_generator(10)
    orientacao = random.choice([-1,0,1])
    
    return e.Lider(nome,orientacao)

def createPais(nome, mundo):
    """
        Funcão que instancia um Pais
        :param nome: nome do país
        :param mundo: endereço para a instância do mundo
        :return: uma instância de um País
    """
    continente = random.choice(['C1','C2','C3'])
    setorEconomico = createSetorEconomico()
    setorMilitar = createSetorMilitar()
    setorPrivado = createSetorPrivado()
    lider = createLider()

    return e.Pais(nome,
    continente, setorEconomico, setorMilitar,
    setorPrivado, lider, mundo)
   
def createInteracaoFixa(mundo):
    """
        Funcão que instancia uma InteracaoFixa
        :param mundo: endereço para uma instância do mundo
        :return: uma instância de uma InteracaoFixa
    """
    escolhida = random.choice([e.InteracaoMilitar, e.InteracaoPrivada, e.InteracaoEconomica])
    paises = mundo.paisesAleatorios() # Remover jogador desse conjunto
    inicio = mundo.ano
    vigencia = np.random.randint(1,20)
    fator = np.random.rand()
    
    interacao = escolhida(paises, inicio, vigencia, fator)
    mundo.interacoesFixas.append(interacao)
    
    return interacao


def createAcaoAleatoria(mundo):
    """
    Cria e executa ação aleatória
    :param mundo:
    :return:
    """
    print([p for p in mundo.paises.keys()])
    input()
    ator = random.choice([p for p in mundo.paises.keys()])
    print('ator', ator)
    print([p for p in mundo.paises.keys()])
    input()
    alvo = random.choice([p for p in mundo.paises.keys()])
    ator = mundo.paises[ator]
    alvo = mundo.paises[alvo]
    fator = np.random.rand()
    nomePanorama = random.choice(['militar','privado','economico'])
    AcaoAleatoria = e.Acao('Acao Repentina',ator, nomePanorama)
    AcaoAleatoria.fazerEfeito(alvo, fator)
